# EX05 Pies

Selles ülesandes tegeleme failide lugemise ja kirjutamisega.

Enne kui hakkame tööle, vaatame, kuidas toimub failide töötlemine pythonis.

## Teooria

Kujutame ette, et meil on olemas fail `example.txt` järgmise sisuga:

```text
Hello, World!
Have a nice day.
```

Meie tahame töödelda faili sisu, kasutades pythonit. Kuidas me seda teeme?

### Faili avamine

Enne, kui hakkame tegelema faili sisu lugemise ja töötlemisega, peame faili avama. Pythonis on selle jaoks olemas sisseehitatud meetod `open()`:

```python
file_object = open('filename', 'mode')
```

* **filename** - tähistab faili nime koos tüübiga (*extension*).
Meie näitefaili puhul oleks see `'example.txt'`, mitte ainult `'example'`. On võimalik panna ka faili täispikka teekonna (`'C:\directory\taltech\file.txt'`).\
**NB!** Pyhtonis tähistab `\` erisümboli algust.
Antud näites oleks faili nimeks ``'C:\directory  altech\file.txt'``, kuna erisümbol `\t` tähistab TABi.
Erisümbolite vältimiseks võib näiteks panna kaks kaldkriipsu `'C:\\directory\\taltech\\file.txt''` või kasutada
spetsiaalset *flag*i `r'C:\directory\taltech\file.txt''`, mis muudab kõik sümbolid sõnasõnalisteks (*raw string*).

* **mode** - tähistab, mida tuleb antud failiga teha. Vaikimisi on selle väärtuseks `r` ehk **read**. Muud võimalikud väärtused:

  * `r` ehk **read** - faili sisu lugemine;
  * `w` ehk **write** - faili kirjutamine. Selle režiimiga kaasneb faili sisu üle kirjutamine;
  * `a` ehk **append** - faili kirjutamine ilma eelneva sisu üle kirjutamata. Uus sisu lisatakse faili lõppu;
  * `r+` ehk **read/write** - faili lugemine ja muutmine. Kirjutab eelmist sisu üle;
  * `a+` ehk **append and read** - faili lugemine ja uue sisu lisamine. Ei kirjuta eelmist sisu üle.

`open()` meetod tagastab **faili objekti** (*file object*), millest(sse) edasi saab lugeda(kirjutada) andmeid. Kui faili pole olemas, seda luuakse ja avatakse automaatselt, Te ei pea faili ise looma.

### Failist lugemine

Nüüd kui fail sai avatud, saame hakata tegelema selle sisu lugemisega. Failist lugemine on võimalik järgmistel viisidel:

* `read(size)` - loeb sisse **size** baiti (sümbolit) ning tagastab need. Juhul, kui **size** pole määratud, loeb terve faili sisu.

  ```python
  file_object = open('example.txt', 'r')  # Avame faili lugemiseks

  print(file_object.read())  # Loeme terve faili sisu

  file_object.seek(0)  # Tagasi faili algusesse (sellest on juttu allpool)

  print(file_object.read(5))  # Loeme esimesed 5 baiti
  print(file_object.read(5))  # Loeme järgmised 5 baiti
  ```

  Väljund:

  ```text
  Hello, World!
  Have a nice day.

  Hello
  , Wor
  ```

* `readline(size)` - kui **size** pole määratud, tagastab ühe rea, liikudes ülevalt alla (ehk esimesel kutsel tagastab esimest rida, teisel teist jne kuni faili lõpuni). Vastasel juhul tagastab järgmised **size** baiti.

  ```python
  file_object = open('example.txt', 'r')

  print(file_object.readline())
  print(file_object.readline(5))
  ```

  Väljund:

  ```text
  Hello, World!
  Have
  ```

* `readlines(hint)` - tagastab `list` objekti koos kõikide failis olevate ridadega. **hint** määrab, kui palju ridu tuleb loendisse panna. Selle analoogiks võib kasutada ka `list(file_object)` kirjapilti, mis samuti tagastab loendi koos kõikide ridadega.

  ```python
  file_object = open('example.txt', 'r')

  print(file_object.readlines())
  ```

  Väljund:

  ```text
  ['Hello, World!\n', 'Have a nice day.']
  ```

* **Tavaline itereerimine** - kõiki ridu saab kätte ka tavalise itereerimise kaudu.

  ```python
  file_object = open('example.txt', 'r')

  for line in file_object:
    print(line)
  ```

  Väljund:

  ```text
  Hello, World!
  Have a nice day.
  ```

### Faili kirjutamine

Faili kirjutamist teostatakse meetodi `write()` abil. Meetod võtab vastu `str` objekti, seega kui on vaja kirjutada näiteks mingisuguse arvu, peame seda alguses muutma sõneks.

```python
file_object = open('example.txt', 'w')  # Avame faili kirjutamiseks

file_object.write('This is a new line.')
file_object.close()  # Sulgeme faili (sellest on juttu allpool)
```

Meie `example.txt` fail näeb nüüd selline välja:

```text
This is a new line.
```

Pange tähele, kuidas kogu eelmine tekst kirjutati üle uue tekstiga. See tuleneb sellest, et me kasutasime `w` ehk **write** režiimi. Selleks, et lisada teksti ilma kogu faili sisu üle kirjutamata, tuleb kasutada
`a+` režiimi.

```python
file_object = open('example.txt', 'a+')

file_object.write('\nThis is appended line.')
file_object.close()
```

Erisümbol (*string literal*) `\n` ehk *line break* ehk **reavahetus** on selle jaoks, et meie lisatud tekst asuks uuel real. Faili sisu on nüüd:

```text
This is a new line.
This is appended line.
```

### Faili sulgemine

Faili tuleb peale sellega töötamist sulgeda. Seda saab teha käsitsi, kasutades meetodit `close()`.

```python
file_object = open('example.txt', 'r')  # Avame faili

print(file_object.read(5))  # Loeme esimesed 5 baiti
file_object.close()  # Sulgeme faili
print(file_object.read())  # Proovime faili sisu lugeda (peaks tulema ValueError)
```

Väljund:

```text
This
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: I/O operation on closed file.
```

Nagu näha, peale seda, kui faili suletakse, ei saa sellega enam midagi teha.

Samuti võib kasutada spetsiaalse `with` kontekstihalduri (*context manager*), mis paneb faili automaatselt kinni peale sellega töö lõpetamist.

```python
with open('example.txt', 'r') as file:
    print(file.read())
print(file.closed)
```

Väljund:

```text
This is a new line.
This is appended line.
True
```

### Meetodid `seek()` ja `tell()`

Failist lugemine ja faili kirjutamine toimub osuti (*pointer*) abil. Kui toimub failist lugemine, on *pointer* asutatud faili algusesse, kuid näiteks teksti lisamise (`a`) režiimis asub *pointer* faili lõpus.

Selleks, et saada teada praeguse *pointer*i positsiooni, kasutatakse meetodit `tell()`. See meetod tagastab baitide arvu, mis näitavad, kaugel on *pointer* faili algusest.

```python
with open('example.txt', 'r') as file:
    file.read(5)  # Loeme esimesed 5 sümbolit
    print(file.tell())  # -> Väljundisse tuleb number 5
```

*Pointer*it saab liigutada. See on teostatav meetodi `seek()` abil. Meetodis on defineeritud kaks parameetrit:

1. **offset** - määrab ära, kui palju sümboleid ette või taha on vaja *pointer*it liigutada.
2. **whence** - positsioon, mille suhtes on vaja *pointer*it liigutada. Tagastab uue *pointer*i positsiooni. Võimalikud väärtused:

    * 0 - faili algus (vaikimisi väärtus). *offset* peab olema suurem või võrdne nulliga;
    * 1 - praegune *pointer*i asukoht. *offset* võib olla negatiivne;
    * 2 - faili lõpp. *offset* on tavaliselt negatiivne.

```python
with open('example.txt', 'r') as file:
    print(file.tell())  # -> 0 (asume faili alguses)
    print(file.seek(5))  # -> 5 (liikusime 5 sümbolit ette)
    print(file.seek(2, 1))  # -> 7 (liikusime veel kaks sümbolit ette praeguse positsiooni suhtes)
    print(file.seek(2))  # -> 2 (liikusime 2 sümbolit ette faili alguse suhtes)
    print(file.read(5))  # -> is is
```

### `.csv` failid

*Comma-Separated-Values* ehk **CSV** on failitüüp, kus andmete eraldamiseks teineteisest kasutatakse koma (vajadusel saab kasutada ka muud sobivat sümbolit). CSV faili võib vaadela tabelina, kus on olemas read ja veergud. Veergude päised on üldjuhul defineeritud faili esimeses reas ning edasi tulevad andmed.

![Näide csv failist](https://srv-file6.gofile.io/download/iS2iJQ/csv_example.JPG)

Pyhton pakub CSV failide töötlemiseks sisseehitatud mooduli originaalse nimega `csv`. Peamised kaks meetodit, mida kasutame:

* `csv.reader()` - võimaldab CSV faili lugeda. Tagastab `reader` objekti, mis itereerib üle failis olevate ridade ning iga rea lugemisel tagastab `list` objekti koos selle rea väärtustega.

    ```python
    import csv  # Impordime csv mooduli

    with open('csv_example.csv', 'r', newline='') as file:
        reader = csv.reader(file)  # Loome csv.reader objekti
        for row in reader:
            print(row)
    ```

    Väljund:

    ```text
    ['Name', 'Age', 'School']
    ['Bob', '20', 'Tallinn University of Technology']
    ['Lisa', '21', 'Tartu University']
    ['Matthew', '19', 'None']
    ```

* `csv.writer()` - võimaldab CSV faili kirjutada. Kirjutamine toimub meetodi `writerow()` abil, mis võtab vastu `list` objekti, milles on ühe rea sisu õiges järjekorras.

    ```python
    import csv

    with open('new_csv_example.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')  # Loome csv.writer objekti

        writer.writerow(['Name', 'Age', 'School'])
        writer.writerow(['Bob', 20, 'Tallinn University of Technology'])
    ```

    Näite põhjal koostatud fail näeb niimoodi välja:

    ![Uus csv fail](https://srv-file6.gofile.io/download/iS2iJQ/new_csv_example.JPG)

Mõned tähelepanekud:

1. Antud näidetes andsime `open()` meetodile kaasa veel ühe argumendi `newline`. Sellest saate lugeda näiteks [siit](https://pythonconquerstheuniverse.wordpress.com/2011/05/08/newline-conversion-in-python-3/). Lühidalt kokku võttes on seda vaja selleks, et python õigesti interpreteeriks failis olevad reavahetused.

2. `delimiter` määrab ära, mis sümbolit kasutatakse andemte eraldamiseks. Mõlemad meetodid aktsepteerivad seda. Vaikimisi on selle väärtuseks koma.

### Sõnastik (`dict`)

Selles ülesandes peate tegelema ka sellise pythoni andmestruktuuriga nagu sõnastik ehk `dict`. Infot sellest, kuidas töötada sõnastikega, leiate [pydocist](https://ained.ttu.ee/pydoc/dict.html). Sõnastiku [sorteerimine](https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/), sorteerimine [mitme võtme järgi](https://stackoverflow.com/questions/34170515/sort-dictionary-by-multiple-values).

## Ülesanne

Fail Gitis: `ex05_pies/pies.py`

### Taust

Kujutage ette, et Teid paluti korrastada ühe võistluse tulemusi. Võistluses osalenud inimesed pidid sööma kooke aja peale. Võitjaks valitakse see, kes suudab kõige rohkem kooke ära süüa. Kahjuks, kui võistlus sai läbi ning tuli aeg tulemusi üle vaadata, pandi tähele, et mõned inimesed pole ennast enne võistluse algust registreerinud ehk nad osalesid illegaalselt. Võistluse korraldajatel ei olnud aega ega jaksu "valesid" osalejaid tulemuste listist eemaldada. Teie ülesandeks ongi leida "õiged" osalejad ning hiljem õigete tulemuste põhjal võitja välja selgitada.

### Sisu

Teile on antud kaks faili:

1. [*Competitors_list*](https://srv-file6.gofile.io/download/iS2iJQ/results.txt) - siin on nimekiri registreeritud osalejatest. Formaat: `Eesnini Perenimi`.

2. [*Results*](https://srv-file6.gofile.io/download/d6jl05/results.txt) - siin on võistluse tulemused. Formaat: `Eesnimi Perenimi - tulemus`.

Teie peate realiseerima järgmised meetodid:

* `get_competitors_list(filename) -> list` - võtab vastu faili nime, mis hoiab endas osalejate nimed ning tagastab järjendi koos nimedega;

* `get_results_dict(filename) -> dict` - võtab vastu faili nime, mis hoiab endas tulemused ning tagastab `dict` objekti, kus nimed on võtmed ja tulemused on väärtused.

* `competitors_filter(competitors_list: str, results: str) -> dict` - parameeter `competitors_list` on faili nimi, mis hoiab endas osalejate nimed ning `results` on faili nimi, mis hoiab endas tulemused. Peab eemaldama tulemustest illegaalsete osalejate nimed ja tulemused. Illegaalne osaleja on see, kelle nime pole registreeritud osalejate nimekirjas. Peab kasutama meetodeid `get_competitors_list` ja `get_results_dict`.

* `sort_results(competitors_list: list, results: dict) -> dict` - võtab vastu järjendi koos osalejate nimedega ja filtreeritud tulemuste sõnastiku. Sorteerib tulemusi nii, et inimene, kes sõi rohkem kooke, asub eespool. Kui mitmel inimesel on sama söödud kookide arv, siis kõrgemat kohta saab see, kes on registreeritud osalejate nimekirjas eespool. Näiteks kui Mati tulemus on 5 kooki ja Kati tulemus on 5 kooki ning Kati asub nimekirjas eespool, siis kõrgemat kohta saab Kati (näiteks Kati saab 4nda koha ja Mati saab 5nda).

* `announce_winner(results: dict) -> str` - võtab vastu filtreeritud tulemuste sõnastiku ning kuulutab välja võitja. Võitja on see inimene, kes suutis kõige rohkem kooke ära süüa. Tagastab sõne kujul `'The winner of the "Pie Eating Competition" is {name} with {result} pies eaten.'`, kus `{name}` on asendatud võitja nimega ja `{results}` tema tulemusega.

* `write_results_csv(competitors_list: str, results: str, file_to_write) -> None` - võtab vastu registreeritud osalejate nimekirja faili nime, tulemuste faili nime ja faili nime, kuhu filtreeritud ja sorteeritud tulemused kirjutada. Uues tulemuste failis on kolm veergu:

    1. **Place** - osaleja koht;
    2. **Name** - osaleja nimi;
    3. **Result** - osaleja saadud tulemus.

    Selles meetodis tuleks kasutada meetodeid `competitors_filter` ja `sort_results`.

### Mall

```python
"""Pies Eating Competition."""
import csv


def get_competitors_list(filename) -> list:
    """
    Get the names of all registered competitors.

    :param filename: is the path to the file with the names of competitors.
    :return: a list containing the names of competitors.
    """
    pass


def get_results_dict(filename) -> dict:
    """
    Get the results and store them in the dictionary.

    Results are following the format 'Firstname Lastname - result'.
    You have to return a dict, where the names of the competitors
    are keys and the results are values.

    :param filename: is the path to the file with the results.
    :return: a dict containing names as keys and results as values.
    """
    pass


def competitors_filter(competitors_list: str, results: str) -> dict:
    """
    Filter out all illegal competitors.

    Illegal competitor is the one, whose name is not in the competitors list.
    You have to return a results dict, which doesn't contain illegal competitors results.
    You should use the methods defined above.

    :param competitors_list: is the path to the file with the names of competitors.
    :param results: is the path to the file with the results.
    :return: a dict with correct results.
    """
    pass


def sort_results(competitors_list: list, results: dict) -> dict:
    """
    Sort the filtered results dictionary.

    In order to find the winner you have to sort the results.
    The more pies the competitor has eaten, the better place they get.
    If there are multiple competitors with the same results, the better place
    goes to the one, who is on the higher place in the names list.

    :param competitors_list: is the list of the registered competitors.
    :param results: is the filtered results dictionary.
    :return: a sorted results dictionary.
    """
    pass


def announce_winner(results: dict) -> str:
    """
    Announce the winner of the competition.

    You have to return a string following this format (without curly brackets):
    'The winner of the "Pie Eating Competition" is {name} with {result} pies eaten.'

    :param results: is the filtered results dictionary.
    :return: a correct winner announcement.
    """
    pass


def write_results_csv(competitors_list: str, results: str, file_to_write) -> None:
    """
    Write the results to csv file.

    The csv file must contain three columns:
    1. Place;
    2. Name;
    3. Result.

    This method should use competiors_filter and sort_results methods.

    :param competitors_list: is the path to the file with the names of competitors.
    :param results: is the path to the file with the results.
    :param file_to_write: is the name of the csv file.
    :return: None
    """
    pass

# Some examples:
if __name__ == '__main__':
    # TODO: Add some examples here.
    pass

```

## Viited

* [Ametlik dokumentatsioon failidest](https://docs.python.org/3.7/tutorial/inputoutput.html#reading-and-writing-files)
* [*open()* meetod](https://docs.python.org/3/library/functions.html#open)
* [Failidest lugemine (pydoc)](https://ained.ttu.ee/pydoc/read_from_file.html)
* [Failidesse kirjutamine (pydoc)](https://ained.ttu.ee/pydoc/write_to_file.html)
* [*csv* moodul](https://docs.python.org/3/library/csv.html)
* [Hea *tutorial* failide teemal](https://dbader.org/blog/python-file-io)
* [*String literals*](https://docs.python.org/3/reference/lexical_analysis.html#index-22)
