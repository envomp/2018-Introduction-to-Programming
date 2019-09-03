# EX03 - Checking personal ID code validity

Fail Gitis: `ex03_idcode/id_code.py`

Ülesande eesmärk on teha programm, mis võimaldab kontrollida antud isikukoodi
korrektsust.

**Ülesande tekstis on kaks malli - need mõlemad lähevad samasse faili** `id_code.py`.

## Isikukoodi numbrid, nende tähendused ja piirangud

Isikukood koosneb täpselt **11** numbrist ehk antud sõne pikkus ei saa ületada 11.
Numbrite tähendused:

**esimene** number:

- **1** - aastail 1800-1899 sündinud mees
- **2** - aastail 1800-1899 sündinud naine
- **3** - aastail 1900-1999 sündinud mees
- **4** - aastail 1900-1999 sündinud naine
- **5** - aastail 2000-2099 sündinud mees
- **6** - aastail 2000-2099 sündinud naine

**teine** ja **kolmas** number:

- sünniaasta **2** viimast numbrit _(nt 01, 75 jne kuni 99)_

**neljas** ja **viies** number:

- sünnikuu number _(nt jaanuar - 01, veebruar - 02 jne, kuni 12)_

**kuues** ja **seitsmes** number:

- sünnikuupäeva number _(nt 01, 08, 20 jne kuni 28, 29, 30 või 31 vastavalt
  sünnikuule)_

**kaheksas**, **üheksas** ja **kümnes** number:

- sellel päeval sündinu järjekorranumber _(nt 000, 012 jne kuni 999)_

**üheteistkümnes** number:

- [kontrollnumber](https://et.wikipedia.org/wiki/Isikukood#Kontrollnumber), mis on arv vahemikikus _(1 kuni 9)_, selleks on olemas
  `Kontrollnumbri arvutamise algoritm`.

## Ülesanne

Ülesande peamine eesmärk on teha programm, mis suudab tuvastada, kas tegu on tõelise isikukoodiga.
Programm koosneb mitmest funktsioonist, mis kontrollivad isikukoodis olevad erinevaid numbreid, näiteks sünnikuupäeva.

- `check_your_id(id_code: str)` - peamine funktsioon, mis kasutab teisi loodud
  kontroll-funktsioone, tagastab `True` või `False` peale kõikide tulemuste
  kättesaamist. Sisendiks on isikukood sõne kujul;
- `check_gender_number(gender_number: int)` - kontrollib soo numbrit, tagastab
  `True` või `False`;
- `check_year_number_two_digits(year_number: int)` - kontrollib aasta numbrit,
  tagastab `True` või `False`;
- `check_month_number(month_number: int)` - kontrollib kuu numbrit, tagastab
  `True` või `False`;
- `check_day_number(year_number: int, month_number: int, day_number: int)` -
  kontrollib kuupäeva numbrit; peab kindlasti vaatama seda, millises kuus on 30
  või 31 päeva ja arvestama ka veebruari kuupäevade arvu muutumisega, tagastab `True`
  või `False`;
  **NB! Kontrollides, kas kuus on 30 või 31 päeva, ei tohi lihtsalt
  kirja panna kõik sobivad kuud tingimuslausete sisse, proovige leida kuu numbri
  ja päevade arvu sõltuvust.**
  **NB! Enne liigasta kontrollimist tuleb teisaldada kahekohaline isikukoodi
  aastanumber neljakohaliseks. Selleks võib kasutada funktsioone, mis on mõeldud 
  sõnumi koostamiseks!**
- `check_leap_year(year_number: int)` - abifunktsioon, mis aitab aru saada, kas
  tegemist on liigaastaga või mitte. Selle funktsiooni sisendiks on juba
  **neljakohaline** aasta number. Tagastab `True` või `False`;
- `check_born_order(born_order: int)` - kontrollib sündinu järjekorranumbrit, 
  tagastab `True` või `False`;
- `check_control_number(id_code: str)` - kontrollib kontrollnumbri
  korrektsust kasutades kontrollnumbri arvutamise valemit.
  (`Kontrollnumbri arvutamise algoritm`\_), tagastab `True` või `False`;

## Mall

```
    """Check if given ID code is valid."""


    def check_your_id(id_code: str):
        """
        Check if given ID code is valid and return the result.

        :param id_code: str
        :return: boolean
        """
        pass


    def check_gender_number(gender_number: int):
        """
        Check if given value is correct for gender number in ID code.

        :param gender_number: int
        :return: boolean
        """
        pass


    def check_year_number_two_digits(year_number: int):
        """
        Check if given value is correct for year number in ID code.

        :param year_number: int
        :return: boolean
        """
        pass


    def check_month_number(month_number: int):
        """
        Check if given value is correct for month number in ID code.

        :param month_number: int
        :return: boolean
        """
        pass


    def check_day_number(year_number: int, month_number: int, day_number: int):
        """
        Check if given value is correct for day number in ID code.
        Also, consider leap year and which month has 30 or 31 days.

        :param year_number: int
        :param month_number: int
        :param day_number: int
        :return: boolean
        """
        pass


    def check_leap_year(year_number: int):
        """
        Check if given year is a leap year.

        :param year_number: int
        :return: boolean
        """
        pass


    def check_born_order(born_order: int):
        """
        Check if given value is correct for born order number in ID code.

        :param born_order: int
        :return: boolean
        """
        pass


    def check_control_number(id_code: str):
        """
        Check if given value is correct for control number in ID code.
        Use algorithm made for creating this number.

        :param id_code: string
        :return: boolean
        """
        pass


     def get_data_from_id(id_code: str):
        """
        Get possible information about the person.
        Use given ID code and return a short message.
        Follow the template - This is a (gender) born on (DD.MM.YYYY).

        :param id_code: str
        :return: str
        """
        pass

    def get_gender(gender_number: int):
        """
        Define the gender according to the number from ID code.

        :param gender_number: int
        :return: str
        """
        pass


    def get_full_year(gender_number: int, year: int):
        """
        Define the 4-digit year when given person was born.
        Person gender and year numbers from ID code must help.
        Given year has only two last digits.

        :param gender_number: int
        :param year: int
        :return: int
        """
        pass

    if __name__ == '__main__':
        print("Overall ID check::")
        print(check_your_id("49808270244"))  # -> True
        personal_id = input()  # type your own id in command prompt
        print(check_your_id(personal_id))  # -> True
        print(check_your_id("12345678901"))  # -> False
        print("\nGender number:")
        for i in range(9):
            print(f"{i} {check_gender_number(i)}")
            # 0 -> False
            # 1...6 -> True
            # 7...8 -> False
        print("\nYear number:")
        print(check_year_number_two_digits(100))  # -> False
        print(check_year_number_two_digits(50)  # -> true
        print("\nMonth number:")
        print(check_month_number(2))  # -> True
        print(check_month_number(15)) # -> False
        print("\nDay number:")
        print(check_day_number(5, 12, 25))  # -> True
        print(check_day_number(10, 8, 32))  # -> False
        print(check_leap_year(1804))  # -> True
        print(check_leap_year(1800))  # -> False
        print("\nFebruary check:")
        print(check_day_number(96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
        print(check_day_number(99, 2, 29))  # -> False (February contains 29 days only during leap year)
        print(check_day_number(8, 2, 29))  # -> True
        print("\nMonth contains 30 or 31 days check:")
        print(check_day_number(22, 4, 31))  # -> False (April contains max 30 days)
        print(check_day_number(18, 10, 31))  # -> True
        print(check_day_number(15, 9, 31))  # -> False (September contains max 30 days)
        print("\nBorn order number:")
        print(check_born_order(0))  # -> True
        print(check_born_order(850))  # -> True
        print("\nControl number:")
        print(check_control_number("49808270244"))  # -> True
        print(check_control_number("60109200187"))  # -> False, it must be 6

        print("\nFull message:")
        print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998"
        print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
        print(get_full_year(1, 28))  # -> 1828
        print(get_full_year(4, 85))  # -> 1985
        print(get_full_year(5, 1))  # -> 2001
        print(get_gender(2))  # -> "female"
        print(get_gender(5))  # -> "male"

```

Funktsioonid lühikese info sõnumi koostamiseks
##############################################

**NB! Kõigepealt on soovitav lugeda** `[sõne vormindamisest](https://ained.ttu.ee/pydoc/string.html?highlight=format#vormindamise-stiil-f-string)

- [Real Python sõne vormindamisest põhjalik artikkel](https://realpython.com/python-strings/)
- [Ametlik Python dokumentatsioon](https://docs.python.org/3/library/stdtypes.html#str)

Sõnumi koostamine on ka ülesande kohustuslik osa, ilma selleta ei saa teste
edukalt läbida! Lisaks, mõned nendest võivad olla abiks põhiülesande lahendamisel.

## Näide

```

    def introduce_yourself(your_name):
        """
        Insert given name into the template to get the greeting.

        :param your_name: string
        :return: string
        """
        return f"Hello everyone, my name is {your_name}"


    if __name__ == '__main__':
        print(introduce_yourself("Bob") -> # Hello everyone, my name is Bob
```

- `get_data_from_id(id_code: str)` - peamine funktsioon, mis kogub infot
  abifunktsioonidest, tagastab `string` - **This is a (sugu) born on
  (sünnikuupäev kujul DD.MM.YYYY)**;

  **NB!** _Kindlasti tuleb veenduda, et antud isikukood on korrektne enne
  sõnumi koostamist (teil on selleks juba olemas funktsioon `check_your_id`._
  Kui isikukood ei ole korrektne, funktsioon peab tagastama -
  **Given invalid ID code!**

- `get_gender(gender_number: int)` - tuvastab sugu isikukoodi esimese numbri põhjal,
  tagastab `string` - **female** või **male**;

- `get_full_year(gender_number: int, year: int)` - tuvastab isikukoodi aasta ja soo numbrite
  abil 4-kohalist aastanumbrit - **18--**, **19--** või **20--**;

## Kontrollnumbri arvutamise algoritm

Liidetakse kokku esimese kümne numbri **1, 2, 3, 4, 5, 6, 7, 8, 9** korrutised
igale arvule vastava järjekorranumbriga _(nt 1×4 + 2×9 + 3×8 jne kuni kümnes
number × jälle 1)_ ning leitakse saadud summast **jääk** jagamisel **11-ga**.
See jääk ongi kontrollnumber.

**NB!** Juhul, kui jääk on võrdne 10-ga, tehakse arvutus uuesti ning võetakse
teguriteks, millega isikukoodi numbreid korrutada, vastavalt
**3, 4, 5, 6, 7, 8, 9, 1, 2, 3**. Leitakse jääk
jagamisel 11-ga. Ja see ongi kontrollnumber.

Kui jääk jälle võrdub 10ga, siis määratakse kontrollnumbriks **0**.

Näide:
isikukoodi 49808270244 kontrollnumber peab olema 4.

1. Summa 1×4 + 2×9 + 3×8 + 4×0 + 5×8 + 6×2 + 7×7 + 8×0 + 9×2 + 1×4 = 169
2. 169 ÷ 11 = 15, jääk 4

Seega on kaks komplekti kordajaid, mida kontrollnumbri leidmisel tuleb kasutada:

- kordajad_1 = (1,2,3,4,5,6,7,8,9,1)
- kordajad_2 = (3,4,5,6,7,8,9,1,2,3)

## Vihjed ja soovitused

**1. Kuupäevade arv igas kuus:**

- Jaanuar 31
- Veebruar 28/29
- Märts 31
- Aprill 30
- Mai 31
- Juuni 30
- Juuli 31
- August 31
- September 30
- Oktoober 31
- November 30
- Detsember 31

**2. int** või **string**

Kuna isikukood antakse `string` tüüpi sisendina, siis tehes . Kui abifunktsioonis on kindlasti teada, et ei pea
opereerima `int` tüübi objektiga, siis pole mõtet seda numbrit konvertida

**3. Liigaasta** ja selle leidmine

Aasta on liigaasta, kui aastaarv jagub 4-ga, välja arvatud juhul, kui ta jagub
100-ga, ent mitte 400-ga.
Natukene lühidam seletus:

1. Kõikide aastade numbrid, mis jaguvad **400-ga**, kõik need **on** kindlasti **liigaastad**
2. Kõik ülejäänude aastade numbrid, mis jaguvad **100-ga**, **ei ole** liigaastad
3. Kõik ülejäänud aastade numbrid, mis jaguvad **4-ga**, kõik need **on** ka **liigaastad**

Liigaastad **on**: 4, 40, 2016, 2000, 1600

Liigaastad **pole**: 3, 41, 2018, 1900, 1800

## Kasulikud lingid

- [sõne (string)](https://ained.ttu.ee/pydoc/string.html)
- [matemaatilised avaldised](https://ained.ttu.ee/pydoc/math.html)
- [funktsiooni argumendid ja parameetrid](https://ained.ttu.ee/pydoc/func.html)
- [tingimuslause](https://ained.ttu.ee/pydoc/if_statements.html)
- [tsükkel](https://ained.ttu.ee/pydoc/loop.html)
