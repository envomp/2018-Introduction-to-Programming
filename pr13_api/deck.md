# PR13

## Teooria

### API

API (Application Programming Interface) ehk Rakendusliides on üheselt määratud moodus
erinevate rakenduste omavaheliseks suhtlemiseks. 

Antud ülesandes kasutame json api-t.

### JSON

JSON (JavaScript Object Notation) on lihtsustatud andmevahetusvorming, mis põhineb JavaScripti programmeerimiskeelel.
Json api on laialdaselt kasutatav, kuna see on inimesele suhteliselt lihtsalt loetav ning ühildub hästi veebirakendustega, mis kasutavad JavaScripti.
Lisaks on enamikes tänapäeval kasutatavates keeltes olemas teegid jsoni mugavaks kasutamiseks.
Püütonisse on json juba sisse ehitatud, seega teeke lisada pole vaja.

## Ülesanne

### Taust

Selle nädala kodutööks (ex13) on kirjutada lihtne Blackjack kaardimäng.
See mäng kasutab võimaluse korral internetis tasuta saadaval olevat API-t (http://deckofcardsapi.com/) 
mille mugavaks kasutamiseks tuleb sul kirjutada klassid `Card` ja `Deck`

### Sisu

#### Klass Card
Lihtne klass andmete hoidmiseks. Sisendväärtuseid ei pea kontrollima.

`def __init__(self, value: str, suit: str, code: str):`
Konstruktor teeb kaardi objekti, võttes sisendparameetriteks kaardi väärtuse, masti ja koodi. 
Väärtused peab salvestama sama nimega isendiväljadele (card, suit, code).

`def __repr(self)__ -> str:`
Tagastab code-väljal oleva väärtuse.

`def __eq__(self, other) -> bool:`
Võrdleb card objekti teise objectiga. Tagastab True, kui teine object on card tüüpi ja sama masti ning väärtusega


Kaardi objektil peavad olema defineeritud järgnevad isendimuutujad:

**value: str**
Kaardi väärtus. Kuulub hulka:

```python
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
```

**suit: str**
Kaardi mast. Kuulub hulka:

```python
suits = ['SPADES', 'DIAMONDS', 'HEARTS', 'CLUBS']
```

**code: str**
Kaardi kood. Kood kombineerib kaardi väärtuse ja masti. Kuulub hulka:
````python
codes = {'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS',
'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD',
'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC',
'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH'}
````

#### Klass Deck

**Info API kohta:  http://deckofcardsapi.com/**

`def __init__(self, deck_count: int = 1, shuffle: bool = False):` Konstruktor teeb deck objekti. Saab sisendiks pakkide
 arvu (mitu 52 kaardist pakki on) ja boolean muutuja, mis määrab, kas deckid peavad olema segatud või ei.
 Salvestada tuleb deck_count ning ka shuffeled väärtused. Viimase salvestamiseks kasutata muutujat nimega
 `is_shuffled` Lisaks peab muutujas nimega `remaining` hoidma kaardipakis olevate kaartide arvu (võib kasutada ka propertid)
 Kaardipaki genereerimiseks kasutada *https://deckofcardsapi.com/api/deck/new/?deck_count={n}* või
  *https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={n}*
 
 Kuna klass peab toimima ka ilma interneti ühenduseta, siis on mõttekas valmis genereerida ka n-ö tagavara
 kaardipakk, mida saaks kasutada kui api lõpetab töötamise. Tagavara kaardipakk salvestada muutujasse `_backup_deck`
 
 `def shuffle(self) -> None:` Segab kaardipaki, kasutada *https://deckofcardsapi.com/api/deck/<<deck_id>>/shuffle/*
 
 `def draw_card(self) -> Card:` Tagastab kaardi kasutades API-t. Kui api ei tööta tuleb tagastada suvaline sobiv kaart
 ise. Et vältida olukorda, kus tagastatakse ühte kaarti korduvalt on mõistlik tagastada neid eelnevalt 
 valmis genereeritud tagavara kaardipakist. Kasutada *https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count={n}*
 
 `def _request(self, url: str):` Saab sisendiks URL-i, millele saata päring.
 Päringute tegemiseks soovitatav kasutada `requests` teeki (olemas ka testeris)
 Eduka päringu korral peaks salvestama `deck_id` -> `id` ning `shuffled` ja `remaining` väljade väärtused 
 samanimelistesse muutujatesse
 **Tagastada tuleb json objekt**

### Mall

```python
"""Deck."""
import requests


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        """Constructor."""

    def __repr__(self) -> str:
        """Repr."""
        return ""

    def __eq__(self, o) -> bool:
        """Eq."""
        return False


class Deck:
    """Deck."""

    DECK_BASE_API = "https://deckofcardsapi.com/api/deck/"

    def __init__(self, deck_count: int = 1, shuffle: bool = False):
        """Constructor."""
        self._backup_deck = []
        self.remaining = -1
        pass

    def shuffle(self) -> None:
        """Shuffle the deck."""
        pass

    def draw_card(self) -> Card:
        """
        Draw card from the deck.

        :return: card instance.
        """
        pass

    def _request(self, url: str):
        """Update deck."""
        pass

    @staticmethod
    def _generate_backup_pile() -> list:
        """Generate backup pile."""
        return []


if __name__ == '__main__':
    d = Deck(shuffle=True)
    print(d.remaining)  # 52
    card1 = d.draw_card()  # Random card
    print(card1 in d._backup_deck)  # False
    print(d._backup_deck)  # 51 shuffled cards
    d2 = Deck(deck_count=2)
    print(d2._backup_deck)  # 104 ordered cards (deck after deck)

```

## Viited

* [Veebist lugemine](https://ained.ttu.ee/pydoc/http_requests.html)
* [JSON](https://ained.ttu.ee/pydoc/json.html)
