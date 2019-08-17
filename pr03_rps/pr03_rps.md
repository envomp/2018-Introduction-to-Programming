# PR 03 

## Teooria

Selle nädala teemaks on sõne. Ülesanede eesmärgiks on anda põgus ülevaade, kuidas töödelda ja vorminada sõnesid (*stringe*). 


## Ülesanne

* funktsioon `ask_user_name`, mis küsib kasutaja nime ja tagastab nime korrektselt näiteks: 
```
ask_user_name('kristjan') # Kristjan
ask_user_name('KRISTJAN') # Kristjan
```
Nimi võib koosneda ainult tähtedest, ei tohi sisaldada tühikuid ja ei tohi olla pikem kui kümme tähte.
```
ask_user_name('kristjan123312') # You entered a wrong name
ask_user_name('KRISTJANKRISTJANKRISTJAN') # You entered a name that is too long
ask_user_name('KRISTJAN KRISTJAN') # You entered a name that has a space
```
* funktsioon `reverse_name`, mis küsib kasuaja nime ja pöörab selle tagurpidi. NB! Oluline oleks, et ümberpööratud nimi algaks suure tähega. 

```
reverse_name('iris') # Siri
```

* funktsioon `ask_user_choice`, mis küsib kasutaja valikut. Valik on järgnev - 'rock', 'paper', 'scissors', kuid tuleb tähele panna, et korrektne on ka 'ROCK'
* funktsioon `determine_winner`, saab sisendiks mängija nime, mängija valiku ja arvuti valiku. Funktsioon tagastab sõne, mis on järgneva malli järgi koostatud. 
`{player_name} had {player_choice} and computer had {computer_choice}, hence {winner} wins.`
Viigi korral tuleks tagastada: `{player_name} had {player_choice} and computer had {computer_choice}, hence it is a draw.`
Kui mingi sisend on ebakorrektne, näiteks kasutaja on oma valikuks sisestanud `water`, siis peaks funktsioon tagastama `There is a problem determining the winner.`

```
print(determine_winner('scissors', 'Marko', 'rock')) # Marko had scissors and computer had rock, hence computer wins.
print(determine_winner('scissors', 'Marko', 'rock')) # Marko had rock and computer had rock, hence it is a draw.
print(determine_winner('scissors', 'Marko', '123')) # There is a problem determining the winner.
```
## Lisa lugemist

### Sõne 

* [Pydoc](https://ained.ttu.ee/pydoc/string.html)
* [Real Python põhjalik tutvustus sõnedest](https://realpython.com/python-strings/)
* [Ametlik Pythoni dokumentatsioon edasijõudnumatele](https://docs.python.org/3/library/string.html) 


### Funktsioon
* [Pydoc](https://ained.ttu.ee/pydoc/func_overview.html) 

