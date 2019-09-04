# Introduction 

Kaust gitis:``pr01_introduction``

Faili nimi: ``introductin.py``

**Abimaterjal**

***Printimine:***

    print("Hello world!")

***Muutujasse salvastamine:***

    university = "taltech"
    
https://ained.ttu.ee/pydoc/variable.html
    
***Stringide liitmine:***

    print("Welcome to " + unversity + "!")
    
https://ained.ttu.ee/pydoc/string.html

***F-string:***
    
    print(f"Hello {university}!")
https://ained.ttu.ee/pydoc/string.html#vormindamise-stiil-f-string

***Inputi kasutamine:***
    
    name = input()
    print("Hello " + name + "!")
    
või
    
    name = input("What's your name? ")

https://ained.ttu.ee/pydoc/input.html
 
***Tingimuslause kasutamine:***

![if statement visualization](https://ained.ttu.ee/pydoc/images/if_statement_visualization.png)

    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")
    
 või
 

    university = "taltech"
    if university == "taltech":
        print("Welcome to taltech")
    elif university == "tu":
        print("Welcome to tu")
    else:
        print("See you next time!")

https://ained.ttu.ee/pydoc/if_statements.html

https://www.w3schools.com/python/python_conditions.asp

**Ülesanne**

Kirjuta lihtne programm, mis küsib kasutajalt nime ja
uurib, kas kasutaja on varem programeerimisega tegelenud. Vastavalt vastustele peab programm andma erineva väljundi.

Programmi algoritm võiks olla järgmine:
1) Kuva ekraanile sõnum ``Hello, my name is Python! Please type your name to continue our conversation.``
2) Küsi kasutajalt nime ja salvesta see muutujasse.(NB! Vali mõistlikud muutujanimed, ära vali ühetähelisi nimesid.)
3) Küsi kasutaja käest, kas ta on varem programmeerimisega tegelenud.
4)
    Kui kasutaja vastab ``Yes``, siis printi ``Congratulations, [Nimi]! It will be a little bit easier for you.``
 
    Kui kasutaja vastab ``No``, siis printi ``Don`t worry, [Nimi]! You will learn everything you need.``
 
    Kui kasutaja vastab midagi muud siis kuva ``Your input is incorrect!``
    

Ülesande jaoks vajalik fail `introduction.py`:

```python
"""My first program."""

```

Stiilinõue on, et failil oleks kirjeldus ehk kommentaar. See on ka kõik, mis teil mallis olemas on.

Lisaks on kasulik lugeda

https://ained.ttu.ee/pydoc/style.html

https://www.w3schools.com/python/python_syntax.asp
