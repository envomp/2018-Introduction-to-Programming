# Geometry

Kaust Gitis: ``ex01_geometry``

Faili nimi: ``geometry.py``

Sinu ülesandeks on luua programm, mis peaks märgatavalt lihtsustama iga algklassiõpilase elu.
Nimelt peab programm küsima kasutaja käest, mis kujundi pindala ta soovib välja arvutada. Seejärel tuleb sisestada vajalikud
mõõtmed (raadius või külje pikkus). Kujundi valikuteks on ring, ruut või kolmnurk (``"circle", "square", "triangle"``).
Ülesande lihtsustamiseks oletame, et kolmurk on võrdkülgne.

Ülesande lahendamise algoritm peab olema järgmine:

1) Programm küsib sisendit ``"Please insert geometric shape:"``
2) Programm küsib kujundi mõõtmed vastavalt sisestatud kujundile.

 Kui sisestatud kujund on ring, siis küsib programm raadiust ``"Please insert radius in cm:"``

 Kui sisestatud kujund on ruut või kolmnurk, siis küsib programm külje pikkust ``"Please insert side length in cm:"``
 
3) Vastavalt sisestatud kujundile peab programm printima saadud pindala koos mõõtühikutega(``"cm^2"``). 


Muul juhul prindib programm ``"Shape is not supported."``

Kui vastuseks ei tule täpne arv, siis tuleb vastust ümardada ``kahe komakohani``.

**Ümardamise kohta saab lugeda [siit](https://ained.ttu.ee/pydoc/math.html#umardamine)**


Näidisväljund:
    
    Please insert geometric shape:triangle
    Please insert side length in cm:3
    The area is 3.9 cm^2
    
    Please insert geometric shape:circle
    Please insert radius in cm:9
    The area is 254.47 cm^2
    
    Please insert geometric shape:square
    Please insert side length in cm:2.25
    The area is 5.06 cm^2
    
**Abimaterjal**
    
***print***

``print`` funktsioon võimaldab printida erinevaid väärtusi konsooli.

    print("Hello") # prints "Hello" to the console

[***Muutuja***](https://ained.ttu.ee/pydoc/variable.html)

Muutujasse on võimalik salvestada erinevaid väärtusi.


    number = 42 # saves int 42 to variable named named number
    print(number) # prints 42 to the console

[***Sisendi lugemine standardsisendist***(``input``)](https://ained.ttu.ee/pydoc/input.html)


``input`` funktsiooniga saab küsida kasutajalt sisendit. Sisendit
küsides tuleb tähele panna, et muutujasse salvestatakse sisestatud
väärtus **sõnena** (``str``).

Näide, kus küsimuse "How old are you" vastus salvestatakse muutujasse ``age``.


    age = input("How old are you?") # waits for user to enter age.

[***Sõne(String) konverteerimine ujukomaarvuks***(``float``)](https://ained.ttu.ee/pydoc/string.html?highlight=konvertida)

    number = float("12.2") # now I can to math with 12.2
    print(number + 3) # prints 15.2

Kui me ei muuda eelnevalt numbreid ujukomaarvuks ``float`` või
täisarvuks ``int``, võib kood visata erindi või käituda veidralt.

    a = "12" + "3"
    print(a) # prints "123"

[***Tingimuslause*** (``if-elif-else``)](https://ained.ttu.ee/pydoc/if_statements.html)

Tingimuslause võimaldab käivitada mingit koodi osa, kui on täidetud
mingi kindel tingimus.

Kõige lihtsam tingimuslause sisaldab võtmesõna ``if`` ja tingimust,
mille tõeseks osutumisel käivitatakse koodiplokk, mis järgneb tingimuslausele.
Näiteks.

    this = "that"
    if this == "that":
        print("This is that.")

Kui me soovime tingimuse mitte täitumisel mingit muud koodi käivitada,
siis kasutame võtmesõna ``else``.

    this = "not that"
    if this == "that": # but this is "not that" so this does not equal "that"
        print("This is that.") # this line is not printed
    else:
        print("This is not that.") # this line is printed

Kui me soovime tingimuse mitte täitumisel proovida, kas mõni muu
tingimus on täidetud, kasutame võtmesõna ``elif``.

    number = 13
    if number > 30:
        print("Number is bigger than 30.")
    elif number <= 0:
        print("Number is less or equal than zero")
    else:
        print("Number is is between 0 and 30.")
        
 
***[Ümardamine](https://ained.ttu.ee/pydoc/math.html#umardamine)***

    print(round(10)) # -> 10
    print(round(10.7)) # -> 11
    print(round(5.5)) # -> 6
    print(round(2.665, 2)) # -> 2.67
       
Lisaks võib lugeda: 

https://www.tutorialsteacher.com/python/math-module

https://www.mathopenref.com/triangleequilateralarea.html

        
***MALL***

```python
"""Ask user a shape and a radius or a side length and calculate the shape area."""

```
   
Stiilinõue on, et failil oleks kirjeldus ehk kommentaar. See on ka kõik, mis teil mallis olemas on.


P.S Ringi pindala välja arvutamisel kasutada konstandi [math.pi](https://ained.ttu.ee/pydoc/math.html#konstantid).