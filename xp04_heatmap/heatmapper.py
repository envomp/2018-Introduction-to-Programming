"""Generate topographic heatmap."""
import topo
import os.path
from PIL import Image, ImageDraw


def generate_map(topo_data: list, width: int, height: int, filename: str) -> bool:
    """
    Generate (heat)map into an image file.

    topo_data comes from topo module. The data is a list
    where every element contains latitude, longitude and altitude (in meters).
    The function should treat coordinates as regular y and x (flat world).
    The image should fill the whole width, height. Every "point" in the data
    should be represented as a rectangle on the image.

    For example, if topo_data has 12 elements (latitude, longitude, altitude):
    10, 10, 1
    10, 12, 1
    10, 14, 2
    12, 10, 1
    12, 12, 3
    12, 14, 1
    14, 10, 6
    14, 12, 9
    14, 14, 12
    16, 10, 1
    16, 12, 1
    16, 14, 3
    and the width = 100, height = 100
    then the first line in data should be represented as a rectangle (0, 0) - (33, 25)
    (x1, y1) - (x2, y2).
    The height is divided into 4, each "point" is 100/4 = 25 pixels high,
    the width is divided into 3, each "point" is 100/3 = 33 pixels wide.
    :param topo_data: list of topography data (from topo module)
    :param width: width of the image
    :param height: height of the image
    :param filename: the file to be written
    :return: True if everything ok, False otherwise
    """
    if not topo_data:
        return False

    max_lon = max(topo_data, key=lambda x: x[1])[1]
    min_lon = min(topo_data, key=lambda x: x[1])[1]
    max_altitude = max(topo_data, key=lambda x: x[2])[2]
    min_altitude = min(topo_data, key=lambda x: x[2])[2]

    cols = round((max_lon - min_lon) / (topo_data[1][1] - topo_data[0][1])) + 1
    rows = int(len(topo_data) / cols)

    lon_step = width / cols
    lat_step = height / rows

    colors = make_colors(min_altitude, max_altitude)

    im = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    for row in range(rows):
        for col in range(cols):
            for meters, color in colors.items():
                if (topo_data[row * cols + col][2]) in meters:
                    break
            draw.rectangle([round(col * lon_step), round(row * lat_step), round(col * lon_step + lon_step),
                            round(row * lat_step + lat_step)], fill=color)

    try:
        im.save(filename)
        return True
    except FileNotFoundError:
        return False


def generate_map_with_coordinates(topo_params: tuple, image_width: int, image_height: int, filename: str) -> bool:
    """
    Given the topo parameters and image parameters, generate map into a file.

    topo_parameters = (min_latitude, max_latitude, latitude_stride, min_longitude, max_longitude, longitude_stride)
    In the case where latitude_stride and/or longitude_stride are 0,
    you have to calculate step yourself, based on the image parameters.
    For example, if image size is 10 x 10, there is no point to query more than 10 x 10 topological points.
    Hint: check the website, there you see "size" for both latitude and longitude.
    Also, read about "stride" (the question mark behind stride in the form).

    Caching:
    if all the topo params are calculated (or given), then it would be wise
    to cache the query results.

    :param topo_params: tuple with parameters for topo query
    :param image_width: image width in pixels
    :param image_height: image height in pixels
    :param filename: filename to store the image
    :return: True, if everything ok, False otherwise
    """
    min_lat, max_lat, lat_str, min_lon, max_lon, lon_str = topo_params

    points_lat = int(1 + abs(max_lat - min_lat) * 120)
    points_lon = int(1 + abs(max_lon - min_lon) * 120)

    if not lat_str:
        lat_str = round(points_lat / image_height) if round(points_lat / image_height) > 1 else 1
    if not lon_str:
        lon_str = round(points_lon / image_width) if round(points_lon / image_width) > 1 else 1

    json_file = f"topo_{min_lat}-{max_lat}-{lat_str}_{min_lon}-{max_lon}-{lon_str}.json"

    if os.path.exists(json_file):
        result = topo.read_json_from_file(json_file)
    else:
        result = topo.read_json_from_web(min_lat, max_lat, lat_str, min_lon, max_lon, lon_str)

        if not result:
            return False

        try:
            with open(json_file, 'w', encoding='utf8') as file:
                file.write(result)
        except FileNotFoundError:
            return False

    topo_data = topo.get_topo_data_from_string(result)

    if topo_data is None:
        return False

    return True if generate_map(topo_data, image_width, image_height, filename) else False


def make_colors(min_alt: int, max_alt: int) -> dict:
    """
    Generate colors dictionary.

    :param min_alt: min altitude
    :param max_alt: max altitude
    :return: colors dictionary
    """
    palette = {}
    if min_alt <= 0 and max_alt <= 0:
        colors_dict(palette, min_alt, max_alt, 0, 5)
    elif min_alt <= 0:
        colors_dict(palette, min_alt, 0, 0, 4)
        colors_dict(palette, 0, max_alt, 5, 9)
    else:
        colors_dict(palette, min_alt, max_alt, 5, 9)

    return palette


def colors_dict(palette: dict, min_alt: int, max_alt: int, low: int, high: int) -> dict:
    """
    Generate altitudes range for colors dictionary.

    :param palette: dict
    :param min_alt: min altitude
    :param max_alt: max altitude
    :param low: lowest color
    :param high: highest color
    :return: colors dictionary
    """
    # 0-4 for negative altitude, 5-9 for positive altitude.
    colors = {
        0: (8, 81, 156),  # dark-blue
        1: (49, 130, 189),  # blue
        2: (107, 174, 214),  # light-blue
        3: (189, 215, 231),  # pale-blue
        4: (239, 243, 255),  # gray
        5: (26, 152, 80),  # green
        6: (166, 217, 106),  # light-green
        7: (255, 255, 191),  # yellow
        8: (253, 174, 97),  # orange
        9: (215, 48, 39)  # red
    }

    step = round((abs(min_alt) + abs(max_alt)) / 5)
    start = min_alt
    for i in range(low, high):
        palette[range(start, start + step)] = colors[i]
        start = start + step
    palette[range(start, max_alt + 1)] = colors[high]

    return palette


if __name__ == '__main__':
    # World min, max -9880, +6372
    # Eesti min, max -138, +286
    # topo_data = topo.get_topo_data_from_string(topo.read_json_from_web(58, 59, 10, 24, 25, 10))
    topo_data = topo.get_topo_data_from_string(topo.read_json_from_file("topo_57.5-60-1_22-29-1.json"))
    # generate_map(topo_data, 100, 100, "mymap.png")
    generate_map_with_coordinates((57.5, 60, 0, 22, 29, 0), 1500, 1000, "eesti.png")
    generate_map_with_coordinates((-89.9, 90, 0, -180, 179.9, 0), 600, 400, "world.png")
