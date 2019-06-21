Ajaplaan
========

Fail Gitis: ``ex06_schedule/schedule.py`` .

Kirjuta programm, mis leiab tekstist kellaajaga märgistatud sõned ja koostab nende põhjal ajaplaani tabeli.

Tabel koostatakse järgmiste reeglite alusel:

- tabelil on kaks veergu, mille pealkirjad on "time" ja "items"
- veeru laius otsustatakse sisu järgi, st veeru laius on kõige laiema sisu laius + 2 (mõlemal pool tühik)
- tabeli päise rea ees (üleval) ja järel (all) on vaid ``-`` (miinus) märkidest koosnev rida
- ülejäänud tabeli ridade ääred ja veergude eraldaja on püstkriips (``|``)
- tabelis on kellaaeg kujul "1:12 PM", "12:00 AM" jne. Vt https://en.wikipedia.org/wiki/12-hour_clock
- tabelis on ajaplaani read sorditud kellaaja järgi kasvavalt (nagu on loogiline ajaplaani koostada)
- tabelis kellaajale vastavad tegevused on väikeste tähtedega (isegi kui tekstis olid suured tähed), korduvaid elemente pole ning tegevused on eraldatud ``, ``
- kui ühtegi ajaplaani sobivat sisendit ei leidu tekstis, kuvatakse sisu ridade all vastav tekst ``No items found``:

.. code-block:: none

    ------------------
    |  time | items  |
    ------------------
    | No items found |
    ------------------

Tekstist loetakse välja järgmised andmed:

- kellaaeg peab sisaldama tunde ja minuteid
- tund võib olla 1- või 2-kohaline (1, 01 ja 11)
- minut võib olla 1- või 2-kohaline (2, 02 ja 22)
- tekstis on kellaaeg 24-tunni formaadis
- minimaalne kellaaeg on 00:00 (või 0:0 või 0,00 või 00-0 jne)
- maksimaalne kellaaeg on 23:59 (või 23!59)
- tunni ja minuti vahel võib olla ükskõik mis eraldaja, välja arvatud number (01:11, 1.2, 6,5, 1a4 on kõik lubatud, 12345 ei ole lubatud
- kellaajale järgnev sõna loetakse selle kellaaja tegevuseks
- kellaaja ja tegevuse vahel võib üks või rohkem tühikut olla
- kellaajale eelneb alati tühik või reavahetus
- tegevus sisaldab vaid ladina tähti, ehk siis tegevus lõppeb seal, kus tuleb mõni mitte ladina täht
  (näiteks "aa,aa" => "aa", "abc2de" => "abc", "tere!" => "tere", "12" => "")
- tabelisse lähevad vaid need tegevused, mille pikkus on vähemalt 1 sümbol


Mall
----

.. code-block:: python

    """Create schedule from the given file."""


    def create_schedule_file(input_filename: str, output_filename: str) -> None:
        """Create schedule file from the given input file."""
        pass


    def create_schedule_string(input_string: str) -> str:
        """Create schedule string from the given input string."""
        pass


    if __name__ == '__main__':
        print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
        create_schedule_file("schedule_input.txt", "schedule_output.txt")

Sisendfail
----------

Näiteks võib proovida sellist sisendfaili:

.. code-block:: none

    A 11:00 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 10:0 a bibendum enim. Praesent dictum
     ante eget turpis tempor, porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae, pulvinar nisl.
     Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. Integer mollis nisi sed fermentum efficitur.
     Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id purus diam. 24:01 Donec blandit,
     est nec semper convallis, arcu libero lacinia ex, eu placerat risus est non tellus.

    Orci varius natoque penatibus et magnis dis 0:12 parturient montes, nascetur ridiculus mus. Curabitur pretium at metus
    eget euismod. Nunc sit amet fermentum urna. Maecenas commodo ex turpis, et malesuada tellus sodales non. Fusce elementum
     eros est. Phasellus nibh magna, tincidunt eget magna nec, rhoncus lobortis dui. Sed fringilla risus a justo tincidunt,
     in tincidunt urna interdum. Morbi varius lobortis tellus, vitae accumsan justo commodo in. 12:001 Nullam eu lorem leo.
     Vestibulum in varius magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
      0:00 Aliquam ac velit sit amet nunc dictum aliquam pulvinar at enim. Nulla aliquam est quis sem laoreet, eu venenatis
      risus hendrerit. Donec ac enim lobortis, bibendum lacus quis, egestas nisi.

    08:01 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros
     lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 18:19 a bibendum enim. Praesent
     dictum ante eget turpis tempor, 00:0 porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae,
     pulvinar nisl. Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. 8:8 Integer mollis nisi sed fermentum
      efficitur. Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id 18:19 purus diam. 18:19
      Donec blandit, est nec semper convallis, arcu 7.01 libero lacinia ex, eu placerat risus est non tellus.

    11:0 lorem
    0:60 bad
    1:2   goodone yes
    15:0 nocomma,
     18:19 yes-minus
      21:59 nopoint.
    23-59 canuseminusthere  22,0 CommaIsAlsoOk
    5:6

Väljund
-------

Sisendfail annab järgmise tulemuse:

.. code-block:: none

    -----------------------------------
    |     time | items                |
    -----------------------------------
    | 12:00 AM | aliquam, porta       |
    | 12:12 AM | parturient           |
    |  1:02 AM | goodone              |
    |  7:01 AM | libero               |
    |  8:01 AM | lorem                |
    |  8:08 AM | integer              |
    | 10:00 AM | a                    |
    | 11:00 AM | lorem                |
    |  3:00 PM | nocomma              |
    |  6:19 PM | a, purus, donec, yes |
    |  9:59 PM | nopoint              |
    | 10:00 PM | commaisalsook        |
    | 11:59 PM | canuseminusthere     |
    -----------------------------------

Ja printimine annab sellise:

.. code-block:: none

    -------------------------
    |     time | items      |
    -------------------------
    | 10:00 AM | pikktekst  |
    | 11:00 AM | teine, jah |
    -------------------------

Vihjeid
-------

Ülesande lahendamiseks on mõistlik vaadata YouTube'ist EX06 kohta käivat videot: https://www.youtube.com/watch?v=GfOsJl-Pmv8

Arutleme, millised sammud oleksid mõistlikud ülesande lahendamiseks:

- luua regulaaravaldis, millega saab kellaaegu leida
- regulaaravaldisega leida kõik kellaajad ja vastavad tegevused
- vajadusel tuleb ebasobivad kellaajad kõrvale jätta
- luua sõnastik, kus kellaaeg on võti ja väärtus on järjend tegevustest (järjend sõnedest, nagu ex05 ülesande puhul)
- sõnastik sorteerida
- koostada sorteeritud tulemuse pealt tabel sõnena ja see tagastada

Vaatame järgnevalt sammu natuke põhjalikumalt.

Regulaaravaldise koostamine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kopeeri näidistekst (see pikem) regex101.com lehele teksiosasse. Nüüd hakka üles regulaaravaldist kirjutama, mis kattuks vaid sobivate kohtadega tekstis. Soovitusi:

- kasuta gruppe (sulge) näiteks tundide ja minutite ümber, sedasi on hiljem lihtsam vastavad väärtused kätte saada
- ei pea tingimata valideerima kõike regexiga. Näiteks tundide/minutite lubatud piiri on pythonis palju lihtsam kontrollida

Regulaaravaldis Pythonisse
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Võta järgnev kood:

.. code-block:: python

    import re

    def create_schedule_string(input_string: str) -> str:
        for match in re.finditer(r"REGEX", input_string):
            print(match)

Seal tsükli sees on sul nüüd olemas kõik need kattumised tekstis, kus muster sobib. See tähendab, et saad loodetavasti kätte kellaaja ja vastava tegevuse. Nüüd sõltub sellest, kas oled gruppe kasutanud või mitte. Kui oled, siis võib-olla piisab täitsa sellest, et saad näiteks tundide arvu kätte ``match.group(1)``, minutite arvu ``match.group(2)`` ja tegevuse ``match.group(3)`` .

See tsükkel on ühtlasi ka koht, kus võid ignoreerida näiteks tundi, mille väärtus on 66.

Sõnastiku loomine
~~~~~~~~~~~~~~~~~~

Eelnevalt loodud tsükli sees on mõistlik hakata täitma sõnastikku. See on väga sarnane ex05 ülesandele. Me proovime koostada sõnastiku, kus kellaajale vastab tegevuste loetelu. Täpsemalt, kellaajale vastab sõnede järjend.

Siinkohal on mõistlik hoida kellaaegu mingil "normaalsel" kujul (mitte 12-tunni formaadis). Näiteks on sobilikud:

- tunnid ja minutid sõnena ja kooloniga. Selleks, et hiljem oleks mugavam sortida, võik ühekohalised olla 0-ga täiendatud. Näiteks: "01:01", "11:00", "12:22" jne.
- minutid arvuna, näiteks 61, 660, 742 jne.
- vms


Seega, kõigepealt peab tsüklis looma võtme. Näiteks võtate tunni ja minuti väärtused ja panete kokku sõnena "01:02".

Kui võti on olemas, tuleb kõigepealt kontrollida, kas selline võti on juba olemas. Kui on, siis tuleb võtme taga olevasse tegevuste nimekirja lisada uus tegevus (välja arvatud ühel juhul - millisel?). Kui võtit pole, tuleb luua selle võtmega uus järjend ja sinna sisse panna käesolev tegevus.

Sõnastiku sortimine
~~~~~~~~~~~~~~~~~~~~~~

Kui eelnevalt on sõnastiku võti valitud selliselt, et selle järgi saab loomulikult sortida, siis peaks see samm olema suhteliselt lihtne. Sortida saab umbes nii: ``sorted_items = sorted(schedule_dict.items(), key=...)``. ``key`` peaks arvatavasti olema lambda funktsioon, mis tagastab, millise väärtuse järgi elemente võrreldakse. Kuna elemendid on ennikud (esimene väärtus on võti, teine väärtus on sõnastiku väärtus sellel kohal), siis tuleks seal tagastada enniku see element, mida võrrelda oleks vaja.

Tähelepanu, sõnastiku sortimisel on tulemus järjend (sõnastik ise ei ole sorditud).

Tabeli koostamine
~~~~~~~~~~~~~~~~~~

Lõpuks tuleb teostada tabeli koostamine. Tuleb tähele panna, et tabel tuleb tastada sõnena, mitte printida.

Mõistlik oleks luua üks järjend, kuhu iga tabeli rida eraldi lisada. Seega esimesena tuleks lisada ülemine "äär": ``table.append("-------")```. Päis ja järgmine "äär" lisatakse umbes samamoodi. Seejärel tabeli sisu osad tuleb lisada vastavalt sorditud ajatabelile. Lõppu lisatakse alumine "äär".

Tabeli veeru laius tuleb arvutada välja vastavalt selles veerus olevale kõige laiemale väärtusele. Tabeli päise tekst on ka väärtus. Seega, kui tabelis on päises "items" ja sisuosas "a" ja "b", siis laius on vastavalt päisele 5. Sellele tuleb lisaks veel mõlemale poole tühik lisada. Tasub vaadata näiteid.

Tabeli veeru vormindamiseks kasutada f-sõne, see ei tee teie koodi väga koledaks. Vihje, f-sõnes saab väärtusi joondada ning arvude puhul saab 0-e ette lisada vastavalt soovile/vajadusele.

Kellaaja konvertimine võiks toimuda alles siin tabeli koostamisel - eelnevalt 12-tunni peale üleminek teeb asjad keeruliseks.
