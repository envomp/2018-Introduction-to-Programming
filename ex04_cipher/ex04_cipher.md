EX04 Cipher
===
Fail Gitis: ex04_cipher/cipher.py

Ülesande eesmärk on kooderida ja dekodeerida tekst ([Rail-fence Cipher](http://practicalcryptography.com/ciphers/classical-era/rail-fence/)).

Sissejuhatus
---
[Rail-fence]((http://practicalcryptography.com/ciphers/classical-era/rail-fence/) (kahjuks ei leidnud eesti keelset varianti) salakiri on lihtne šifreerimismeetod, millega tuleb antud ülesande raames kodeerida ja dekodeerida tekst.
Rail-fence salakirja ideeks on vahetada omavahel tekstis olevad tähed nõnda, et tekiks uus šiffertekst. Kodeerimise ja dekodeerimise jaoks on kõige olulisem salakirjaga kaasa antav võti.

Kodeerimise reeglid ja näited
---
Esialgu vaatame ühes sõna kodeerimist. Kodeerimisega kaasa antav võti määrab mitme "tasandiline" kood meil on. Kui `key=1`, siis on kodeeritud tekst võrdne esialgse teksitga.
```
key = 1
"hello" => "hello"
```
Kui võti on ühest suurem, siis peame paigutama tähed erinevatele ridadele. Oletame, et meil on `key=3 ja str="hello"`.

    1. Paigutame 'h' esimese rea esimesele positsioonile.
    2. Paigutame 'e' teise rea teisele positsioonile.
    3. Paigutame 'l' kolmanda rea kolmandale positsioonile.
    4. Paigutame 'l' teise rea neljandale positsioonile.
    5. Paigutame 'o' esimese rea viiendale positsioonile.
    6. Liidame tähed ridade kaupa kokku. 1 rida + 2 rida + 3 rida.
    
```
h . . . o
. e . l .  => "hoell"
. . l . .
```
Kui oleme tutvunud kodeerimise loogikaga, vaatame pikema teksti kodeerimist. Selleks , et oleks võimalik taastada esialgne tekst asendame tekstis olevad tühikud '_'-ga.
```
"Mind on vaja kodeerida" => "Mind_on_vaja_kodeerida" 
```
Kodeerimisel võtame võtmeks kolme `key=3`.
```
M . . . _ . . . v . . . _ . . . e . . . d .
. i . d . o . _ . a . a . k . d . e . i . a => "M_v_edido_aakdeiannjor"
. . n . . . n . . . j . . . o . . . r . . .
```

Abimaterjalid ülesande lahendamiseks
------------------------------------
- Koodi kirjutamisel vältige koodi kordumist. Selleks kasutage abifunktsioone.
- Üks võimalik lahendsukäik on kodeerimisel luua järjend sõnedest, kus iga element vastab ühele reale.
    ```
    h . . . o
    . e . l .  => ["h...o", ".e.l.", "..l.."]
    . . l . .
    ```
    Edasi saab elemndid liita kokku ning asendada punktid ja võimalikud "_".
    ```python
    rows = ["h...o", ".e.l.", "..l.."]
    string = join(rows) => "h...o.e.l...l.."
    string => replace(".") => replace("_")
    ```
    Pseudokoodis kasutatud meetodid [join](https://www.geeksforgeeks.org/join-function-python/) ja [replace](https://www.geeksforgeeks.org/python-string-replace/)
- Dekodeerimise üks võimalik lahedsukäik on kujutada ette, et teil on kodeeritava sõnega võrdse pikkusega tärnidest koosnev sõne "*".
Paigutate antud tärnid sarnaselt kodeerimisega erinevatesse ridadesse. See annab teile informatsiooni mittu tähte peab minema igasse ritta.
Edasi saab asendada tärnid krüpteeritud tähtedega. Peale seda jääb vaid lugeda tähed sik-sakiliselt.

    ```
                            * . . . *  => 2 => ho
    "hoell" => "*****"  =>  . * . * .  => 2 => el
                            . . * . .  => 1 => l
    
    h . . . o
    . e . l .  => ["h...o", ".e.l.", "..l.."] => "hello"
    . . l . .
    ```
- [sõne](https://ained.ttu.ee/pydoc/string.html)
- [järjend](https://ained.ttu.ee/pydoc/list.html>)
- [tsükkel (loop)](https://ained.ttu.ee/pydoc/loop.html)
- [tingimuslause](https://ained.ttu.ee/pydoc/if_statements.html)

Funktsioonid
---
- `message: string` - krüpteeritav või dekrüpteeritav sõne.
- `key: int` - kodeerimise võti. Täpsemad võtme kasutamise reeglid on kirjeldatud punktis `Kodeerimise reeglid ja näited`.
- `encode(message : str, key: int)` - funktsioon sõne krüpteerimiseks.
- `decode(message : str, key: int)` - funktsioon sõne dekrüpteerimiseks.


Mall:

```python
def encode(message : str, key: int) -> str:
    """
    Encode text using Rail-fence Cipher.
    
    Replace all spaces with '_'.
    :param message : string:
    :param key: int:
    :return: Decoded string.
    """
    pass
    
    
def decode(message : str, key: int) -> str:
    """
    Decode text knowing it was encoded using Rail-fence Cipher.
    
    '_' have to be replaced with spaces.
    :param message : string:
    :param key: int:
    :return: Decoded string.
    """
    pass 
    
    
if __name__ == '__main__':
    print(encode("Mind on vaja krüpteerida", 3))  # => M_v_prido_aaküteiannjred
    print(encode("Mind on", 3))  # => M_idonn
    print(decode("M_idonn", 3))  # => Mind on
    print(decode("M_v_prido_aaküteiannjred", 3))  # => Mind on vaja krüpteerida
```