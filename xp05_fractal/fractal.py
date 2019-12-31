"""Generate fractals."""
import matplotlib.cm as cmap
import matplotlib.pyplot as mpl
import numpy as np
from PIL import Image


class Fractal:
    """Fractal."""

    def __init__(self, size, scale, computation):
        """Constructor.

        Arguments:
        size -- the size of the image as a tuple (x, y)
        scale -- the scale of x and y as a list of 2-tuple
                 [(minimum_x, minimum_y), (maximum_x, maximum_y)]
        computation -- the function used for computing pixel values as a function
        """
        self.width, self.height = size
        (self.minimum_x, self.minimum_y), (self.maximum_x, self.maximum_y) = scale
        self.computation = computation

    def compute(self):
        """Create the fractal by computing every pixel value."""
        self.fractal = [[self.pixel_value((x, y)) for x in range(self.width)] for y in range(self.height)]

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        point_x = (self.maximum_x - self.minimum_x) / (self.width - 1)
        point_y = (self.maximum_y - self.minimum_y) / (self.height - 1)
        x, y = pixel
        return self.computation((x * point_x + self.minimum_x, self.maximum_y - y * point_y))

    def save_image1(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        bitmap = Image.new("RGB", (self.width, self.height), "white")
        pixels = bitmap.load()
        for row in range(self.height):
            for col in range(self.width):
                i = self.fractal[row][col]
                pixels[col, row] = (i << 21) + (i << 10) + i * 8
        bitmap.save(filename)

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        data = np.array(self.fractal)
        mpl.figure(figsize=(self.width * 0.01805, self.height * 0.01805), dpi=72)
        mpl.imshow(data, cmap=cmap.gnuplot)  # jet, rainbow, gnuplot, gnuplot2
        mpl.axis('off')
        mpl.savefig(filename, bbox_inches='tight', pad_inches=0)


if __name__ == "__main__":
    def mandelbrot_computation(pixel):
        """
        The function used for computing Mandelbrot pixel values as a function.

        :param pixel: the pixel coordinate (x, y)
        :return: the number of iterations of computation it took to go out of bounds as integer.
        """
        x, y = pixel
        c = 0
        c0 = np.complex(x, y)
        max_iterations = 50
        for iterations in range(1, max_iterations):
            if abs(c) > 2:
                return iterations
            c = c * c + c0
        return 0

    def julia_computation(pixel):
        """
        The function used for computing Julia pixel values as a function.

        :param pixel:
        :return:
        """
        zx, zy = pixel
        cx, cy = 0.37, 0.16  # (-0.5, 0.56), (-0.7, 0.27015), (0.37, 0.16), (-0.75, 0.25), (0.285, 0.01), (0.279, 0)
        max_iterations = 100
        iterations = 0
        while (zx * zx + zy * zy) < 4 and iterations < max_iterations:
            zx, zy = zx * zx - zy * zy + cx, 2 * zx * zy + cy
            iterations += 1
        return iterations

    # mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    # mandelbrot.compute()
    # mandelbrot.save_image("mandelbrot.png")
    julia = Fractal((1000, 1000), [(-2, -2), (2, 2)], julia_computation)
    julia.compute()
    julia.save_image("julia.png")
    # mandelbrot2 = Fractal((1000, 1000), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    # mandelbrot2.compute()
    # mandelbrot2.save_image("mandelbrot2.png")
