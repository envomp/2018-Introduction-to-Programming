**Geometry**

Sinu esimeseks on ülesnadeks on luua programm, mis peaks märgatavalt lihtsustama iga algklassiõpilase elu.
Nimelt peab programm küsima kasutaja käest, mis kujundi pindalat ta soovib välja arvutada ja siis sisestada vajalikud
mõõtmed (raadius või külje pikkus). Valikuteks on ring, ruut või kolmnurk(``"circle", "square", "triangle"``).
Ülesande lihtsustamiseks oletame, et kolmurk võib olla ainult võrdkülgne.

Ülesande lahendamise algoritm peab olema järgmine:

1) Programm küsib sisendit ``Please insert geometric shape:``
2) Programm küsib kujundi mõõtmed ``Please insert radius or side length in cm:``
3) Vastavalt sisestatud kujundile peab programm printima saadud pindala koos mõõtühikutega(``cm^2``). 
Muul juhul prindib programm ``Shape is not supported.``


Näidisväljund:
    
    Please insert geometric shape:triangle
    Please insert radius or side length in cm:3
    The area is 3.8971143170299736 cm^2
    
    
    Please insert geometric shape:circle
    Please insert radius or side length in cm:9
    The area is 254.34 cm^2
    
***print***

``print`` funktsioon võimaldab printida erinevaid väärtusi konsooli.

    print("Hello") # prints "Hello" to the console

***Muutuja***

<https://ained.ttu.ee/pydoc/variable.html>

Muutujasse on võimalik salvestada erinevaid väärtusi.


    number = 42 # saves int 12 to variable named named number
    print(number) # prints 42 to the console

Sisendi lugemine standardsisendist (``input``)

<https://ained.ttu.ee/pydoc/input.html>

``input`` funktsiooniga saab küsida kasutajalt sisendit. Sisendit
küsides tuleb tähele panna, et muutujasse salvestatakse sisestatud
väärtus **sõnena** (``str``).

Näide, kus küsimuse "How old are you" vastus salvestatakse muutujasse ``age``.


    age = input("How old are you?") # waits for user to enter age.

***Sõne***

<https://ained.ttu.ee/pydoc/string.html?highlight=konvertida>

konverteerimine ujukomaarvuks(``float``).

    number = float("12.2") # now I can to math with 12.2
    print(number + 3) # prints 15.2

Kui me ei muuda eelnevalt numbreid ujukomaarvuks ``float`` või
täisarvuks ``int`` võib kood visata erindi või käituda veidralt.

    a = "12" + "3"
    print(a) # prints "123"

***Tingimuslause*** (``if-elif-else``)
 
 <https://ained.ttu.ee/pydoc/if_statements.html>

Tingimuslause võimaldab käivitada mingit koodi osa, kui on täitetud
mingi kindel tingimus.

Kõige lihtsam tingimuslause sisaldab võtmesõna ``if`` ja tingimust,
mille tõeseks osutumisel käivitatakse koodiblokk, mis järgneb tingimuslausele.
olev kood. Näiteks.

    this = "that"
    if this == "that":
        print("This is that.")

Kui me soovime tingimuse mitte täitumisel mingit muud koodi käivitada
siis kasutame võtmesõna ``else``.

    this = "not that"
    if this == "that": # but this is "not that" so this does not equal "that"
        print("This is that.") # this line is not printed
    else:
        print("This is not that.") # this line is printed

Kui me soovime tingimuse mitte täitumisel proovida, kas mõni muu
tingimus on täitetud kasutame võtmesõna ``elif``.

    number = 13
    if number > 30:
        print("Number is bigger than 30.")
    elif number <= 0:
        print("Number is less or equal than zero")
    else:
        print("Number is is between 0 and 30.")
        
Lisaks võib lugeda: 

https://www.tutorialsteacher.com/python/math-module
https://www.mathopenref.com/triangleequilateralarea.html


        
***MALL***

    import math
    
    def calculate_area():
    """ Ask user wished shape and radius or side length and calculate area."""
    
        #YOUR CODE GOES HERE!
    
    if __name__ == '__main__':
        calculate_area()



P.S Kolmnurga pindala välja arvutamisel piisab kui π on 3.14.