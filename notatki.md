# Spis Treści
1. [Podstawowe elementy składni w Pythonie](#podstawowe-elementy-składni-w-pythonie)
2. [Typy danych i zmienne w Pythonie](#typy-danych-i-zmienne-w-pythonie)
3. [Operatory w Pythonie](#operatory-w-pythonie)
4. [Struktury sterujące w Pythonie](#struktury-sterujące-w-pythonie)
5. [Funkcje w Pythonie](#funkcje-w-pythonie)
6. [Struktury danych w Pythonie](#struktury-danych-w-pythonie)
7. [Operacje wejścia/wyjścia otaz obsługa plików w Pythonie](#operacje-wejściawyjścia-otaz-obsługa-plików-w-pythonie)
8. [Moduły i importy w Pythonie](#moduły-i-importy-w-pythonie)

# Podstawowe elementy składni w Pythonie

### Struktura programu

W Pythonie kod jest wykonywany od góry do dołu, a więc nie ma potrzeby definiowania funkcji main(), jak w C++ czy Java. Jednak konwencjonalnie stosuje się poniższy zapis.
```py
def main():
    print("Witaj w Pythonie!")

if __name__ == "__main__":
    main()
```

Blok `if __name__ == "__main__":` oznacza, że kod w nim zawarty zostanie wykonany tylko wtedy, gdy plik uruchamiany jest bezpośrednio, a nie importowany jako moduł.

### Zasady dotyczące wielkości liter

Python rozróżnia wielkość liter. Oznacza to, że zmienne `zmienna` i `Zmienna` to dwa różne obiekty. To samo dotyczy nazw funkcji i klas.

```py
a = 10
A = 20
print(a)  # 10
print(A)  # 20
```

### Komentarze

```py
# To jest komentarz jednoliniowy
"""
To jest wieloliniowy komentarz,
który może być użyty do opisu kodu.
"""
```

# Typy danych i zmienne w Pythonie

### Deklaracja i inicjalizacja zmiennych

W Pythonie nie trzeba deklarować typu zmiennej – Python sam go określa na podstawie przypisanej wartości.

```py
x = 10              # int
y = 3.14            # float
z = "Hello"         # str
is_python = True    # bool
```
Można też przypisać wiele wartości na raz.
```py
a, b, c = 1, 2.5, "tekst"
```

Typ | Opis|Przykład
--|--|--|
`int`|Liczby całkowite|`x = 42`
`float`|	Liczby zmiennoprzecinkowe|`y = 3.14`
`str`|	Ciągi znaków	|`text = "Python"`
`bool`|	Wartości logiczne	|`flag = True`
`list`|	Lista (tablica dynamiczna)	|`numbers = [1, 2, 3]`
`tuple`|	Krotka (niemutowalna lista)	|`coords = (10, 20)`
`dict`|	Słownik (klucz-wartość)	|`data = {"name": "Alice", "age": 25}`
`set`|	Zbiór unikalnych wartości	|`unique = {1, 2, 3, 3}`

### Sprawdzanie typu zmiennej

Aby sprawdzić typ zmiennej, używamy funkcji type().
```py
x = 10
print(type(x))      # output: <class 'int'>
```

### Konwersja typów

Python pozwala na konwersję między typami.

```py
a = "100"
b = int(a)          # Konwersja na int
c = float(a)        # Konwersja na float
d = str(b)          # Konwersja na string
```

### Stałe

W Pythonie nie ma słowa kluczowego const, ale stosuje się konwencję – nazwy stałych zapisuje się WIELKIMI_LITERAMI. Nie są one chronione przed zmianą, ale konwencja mówi, że nie powinny być modyfikowane.
```py
PI = 3.14159
GRAVITY = 9.81
```

# Operatory w Pythonie

Python obsługuje różne rodzaje operatorów, które służą do wykonywania operacji na zmiennych i wartościach.

### Operatory arytmetyczne

Służą do wykonywania podstawowych operacji matematycznych.

Operator	|Opis	|Przykład (`a = 10`, `b = 3`)	|Wynik
--|--|--|--
`+`	|Dodawanie	|`a + b`	|`13`
`-`	|Odejmowanie	|`a - b`	|`7`
`*`	|Mnożenie	|`a * b`	|`30`
`/`	|Dzielenie (wynik float)	|`a / b`	|`3.3333...`
`//`	|Dzielenie całkowite	|`a // b`	|`3`
`%`	|Reszta z dzielenia (modulo)	|`a % b`	|`1`
`**`	|Potęgowanie	|`a ** b`	|`1000`

### Operatory porównania

Porównują wartości i zwracają `True` lub `False`.

Operator	|Opis	|Przykład (`a = 10`, `b = 3`)	|Wynik
--|--|--|--
`==`	|Równość	|`a == b`	|`False`
`!=`	|Nierówność	|`a != b`	|`True`
`>`	|Większe niż	|`a > b`	|`True`
`<`	|Mniejsze niż	|`a < b`	|`False`
`>=`	|Większe lub równe	|`a >= b`	|`True`
`<=`	|Mniejsze lub równe	|`a <= b`	|`False`

### Operatory logiczne

Służą do operacji na wartościach `True` i `False`.

Operator	|Opis	|Przykład (`x = True`, `y = False`)	|Wynik
--|--|--|--
`and`	|Zwraca `True`, jeśli oba warunki są `True`	|`x and y`	|`False`
`or`	|Zwraca `True`, jeśli przynajmniej jeden warunek jest `True`	|`x or y`	|`True`
`not`	|Negacja wartości logicznej	|`not x`	|`False`

### Operatory bitowe

Działają na poziomie bitów (`0` i `1`).

Operator	|Opis	|Przykład (`a = 5` → `0101`, `b = 3` → `0011`)	|Wynik
--|--|--|--
`&`	|AND bitowy	|`a & b`	|`0001` (1)
`\|`   |OR bitowe: |`a \| b`  |`0111` (7)
`^`	|XOR bitowy	|`a ^ b`	|`0110` (6)
`~`	|Negacja bitowa	|`~a`	|(-6, bo U2 na 32 bit)
`<<`	|Przesunięcie bitowe w lewo	|`a << 1`	|`1010` (10)
`>>`	|Przesunięcie bitowe w prawo	|`a >> 1`	|`0010` (2)

### Operatory przypisania

Skrócony zapis operacji przypisania.

Operator	|Opis	|Przykład (`a = 5`)	|Wynik
--|--|--|--
`=`	|Przypisanie wartości	|`a = 5`	|`a = 5`
`+=`	|Dodanie i przypisanie	|`a += 3`	|`a = 8`
`-=`	|Odjęcie i przypisanie	|`a -= 2`	|`a = 3`
`*=`	|Mnożenie i przypisanie	|`a *= 2`	|`a = 10`
`/=`	|Dzielenie i przypisanie	|`a /= 2`	|`a = 2.5`
`//=`	|Dzielenie całkowite i przypisanie	|`a //= 2`	|`a = 2`
`%=`	|Modulo i przypisanie	|`a %= 3`	|`a = 2`
`**=`	|Potęgowanie i przypisanie	|`a **= 2`	|`a = 25`
`&=`	|AND bitowe i przypisanie	|`a &= 3`	|`a = 1`
`\|=`	|OR bitowe i przypisanie	|`a \|=3`   |`a=7`
`^=`	|XOR bitowe i przypisanie	|`a ^= 3`	|`a = 6`
`<<=`	|Przesunięcie bitowe w lewo i przypisanie	|`a <<= 1`	|`a = 10`
`>>=`	|Przesunięcie bitowe w prawo i przypisanie	|`a >>= 1`	|`a = 2`

# Struktury sterujące w Pythonie

Python obsługuje standardowe konstrukcje sterujące, takie jak instrukcje warunkowe i pętle.

### Instrukcje warunkowe (`if`, `elif`, `else`).

Zasady składni:
1. Brak nawiasów klamrowych – Python używa wcięć do oznaczania bloków kodu.
2. `elif` zamiast `else if` – skrócona wersja w Pythonie.

```py
x = 10

if x > 0:
    print("Liczba jest dodatnia")
elif x < 0:
    print("Liczba jest ujemna")
else:
    print("Liczba to zero")
```

Skrócona wersja warunku (operator trójargumentowy).
```py
x = 10
status = "dodatnia" if x > 0 else "nie-dodatnia"
print(status)       # "dodatnia"
```

### Pętla `for`

Przydatna podczas iteracji po kolekcjach (`list`, `tuple`, `dict`, `set`, `str`).

Przykład iteracji po liście:
```py
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
```

### Pętla `for` z `range()`
Zakresy:
- `range(5)` → `0, 1, 2, 3, 4`
- `range(2, 6)` → `2, 3, 4, 5`
- `range(0, 10, 2)` → `0, 2, 4, 6, 8` (skok co 2)

```py
for i in range(5):  # Generuje liczby od 0 do 4
    print(i)
```

### Pętla `while`

Wykonuje kod, dopóki warunek jest prawdziwy.

```py
x = 0

while x < 5:
    print(x)
    x += 1
```
#### Pętla nieskończona (`while True`)

```py 
while True:
    print("Działa!")
    break           # Przerywa pętlę
```

### `break` i `continue`

- `break` – przerywa pętlę.
- `continue` – pomija resztę kodu i przechodzi do kolejnej iteracji.
```py
for i in range(10):
    if i == 5:
        break       # Przerywa pętlę, gdy i = 5
    print(i)
```
```py
for i in range(5):
    if i == 2:
        continue    # Pomija i = 2
    print(i)
```
# Funkcje w Pythonie
Funkcje w Pythonie pozwalają na grupowanie kodu w bloki, które można wielokrotnie wywoływać.

### Definiowanie funkcji (`def`)
Funkcję tworzymy za pomocą słowa kluczowego `def`.
```py
def powitanie():
    print("Cześć, świecie!")

powitanie()         # Wywołanie funkcji
```
### Funkcja z argumentami
Możemy przekazywać wartości do funkcji jako argumenty.
```py
def powitanie(imie):
    print(f"Cześć, {imie}!")

powitanie("Ania")   # Cześć, Ania!
powitanie("Tomek")  # Cześć, Tomek!
```
### Domyślne wartości argumentów
Jeśli argument nie zostanie podany, użyta zostanie wartość domyślna.
```py
def powitanie(imie="Gość"):
    print(f"Cześć, {imie}!")

powitanie()         # Cześć, Gość!
powitanie("Kasia")  # Cześć, Kasia!
```
### Zwracanie wartości (`return`)
Funkcja może zwracać wartość za pomocą `return`.
```py
def suma(a, b):
    return a + b

wynik = suma(3, 7)
print(wynik)        # 10
```
### Argumenty pozycyjne i nazwane
Pozycyjne (`*args`) – dowolna liczba argumentów.
```py
def suma(*liczby):
    return sum(liczby)

print(suma(1, 2, 3))        # 6
print(suma(5, 10, 15, 20))  # 50
```
Nazwane (`**kwargs`) – argumenty w formie klucz-wartość.
```py
def dane_osoby(**info):
    for klucz, wartosc in info.items():
        print(f"{klucz}: {wartosc}")

dane_osoby(imie="Ania", wiek=25, miasto="Warszawa")
# output:
# imie: Ania
# wiek: 25
# miasto: Warszawa
```
### Funkcje anonimowe (`lambda`)
Służą do definiowania prostych funkcji w jednej linijce.
```py
kwadrat = lambda x: x ** 2
print(kwadrat(5))   # 25
```
### Zasięg zmiennych (`global`, `nonlocal`)
`global` – dostęp do zmiennej globalnej w funkcji.
```py
x = 10

def zmien_x():
    global x
    x = 20

zmien_x()
print(x)            # 20
```
`nonlocal` – zmiana zmiennej w funkcji zagnieżdżonej
```py
def zewnetrzna():
    x = 5
    def wewnetrzna():
        nonlocal x
        x += 1
    wewnetrzna()
    print(x)        # 6

zewnetrzna()
```
# Struktury danych w Pythonie
Python oferuje kilka podstawowych struktur danych: listy, krotki, zbiory i słowniki. Każda z nich ma inne zastosowanie.

## 1. Listy (`list`)

Lista to kolekcja elementów, które mogą być różnego typu. Jest ***mutowalna*** (można zmieniać jej elementy).

Tworzenie listy
```py
liczby = [1, 2, 3, 4, 5]
mieszana = [10, "tekst", 3.14, True]

print(liczby)           # [1, 2, 3, 4, 5]
```
Dodawanie elementów
```py
liczby = [1, 2, 3, 4, 5]
liczby.append(6)        # Dodaje na koniec
print(liczby)           # [1, 2, 3, 4, 5, 6]
liczby.insert(2, 99)    # Wstawia 99 na indeksie 2 
                        # (wszystkie elementy o indeksach większych i równemu temu na które się wstawia zostają zwiększone o 1)
print(liczby)           # [1, 2, 99, 3, 4, 5, 6]
```
Usuwanie elementów
```py
liczby = [1, 2, 3, 4, 5]
liczby.remove(3)        # Usuwa wartość 3
print(liczby)           # [1, 2, 4, 5]
ostatni = liczby.pop()  # Usuwa ostatni element i zwraca go
print(liczby)           # [1, 2, 4]
del liczby[0]           # Usuwa element o indeksie 0
print(liczby)           # [2, 4]
```
Iteracja po liście
```py
for liczba in liczby:
    print(liczba)
```
Filtrowanie listy (`list comprehension`)
```py
kwadraty = [x ** 2 for x in range(5)]
print(kwadraty)         # [0, 1, 4, 9, 16]
```
## 2. Krotki (`tuple`)
Krotki są ***niemutowalne*** – nie można zmieniać ich elementów po utworzeniu.

Tworzenie krotki
```py
krotka = (1, 2, 3, "tekst")
print(krotka[1])        # 2
```
Rozpakowywanie krotek
```py
a, b, c = (10, 20, 30)
print(a, b, c)          # 10 20 30
```
## 3. Zbiory (`set`)
Zbiory przechowują unikalne wartości i są nieuporządkowane.

Tworzenie zbioru
```py
zbior = {1, 2, 3, 3, 4}
print(zbior)            # {1, 2, 3, 4} (duplikaty są usuwane)
```
Operacje na zbiorach
```py
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)            # {1, 2, 3, 4, 5} (suma zbiorów)
print(A & B)            # {3} (część wspólna)
print(A - B)            # {1, 2} (różnica)
```
## 4. Słowniki (`dict`)
Słownik przechowuje dane w postaci ***klucz: wartość***.

Tworzenie słownika
```py
osoba = {"imie": "Ania", "wiek": 25, "miasto": "Warszawa"}
print(osoba["imie"])    # Ania
```
Dodawanie i usuwanie elementów
```py
osoba["email"] = "ania@example.com"     # Dodanie nowej pary
del osoba["wiek"]                       # Usunięcie klucza
```
Iteracja po słowniku
```py
for klucz, wartosc in osoba.items():
    print(f"{klucz}: {wartosc}")
```
# Operacje wejścia/wyjścia otaz obsługa plików w Pythonie
Operacje wejścia (input) i wyjścia (output) są kluczowe w programowaniu – pozwalają na interakcję użytkownika z programem oraz zapis i odczyt danych.

### Odczyt danych od użytkownika (`input()`)

Funkcja `input()` pozwala użytkownikowi wprowadzić dane z klawiatury. Domyślnie zwraca ciąg znaków (`str`).\
Przykład – pobieranie imienia od użytkownika
```py
imie = input("Podaj swoje imię: ")
print("Cześć,", imie)
```
Konwersja danych wejściowych
Jeśli użytkownik podaje liczbę, należy przekonwertować ją na odpowiedni typ.
```py
wiek = int(input("Podaj swój wiek: "))      # Konwersja na int
print("Za 5 lat będziesz miał", wiek + 5)
```
### Wyjście danych (`print()`)
Funkcja `print()` pozwala wyświetlić dane na ekranie.
```py
print("Witaj w programie!")
```
### Łączenie wielu argumentów (`sep`, `end`)
```py
print("Imię:", "Anna", sep="-")             # Imię:-Anna
print("Linia 1", end=" ")                   # end="" nie dodaje nowej linii
print("Linia 2")                            # Linia 1 Linia 2
```
### Formatowanie ciągów znaków (`f-stringi`)
```py
imie = "Jan"
wiek = 30
print(f"{imie} ma {wiek} lat.")  # Jan ma 30 lat.
```
### Operacje na plikach
Python pozwala na łatwe otwieranie, odczytywanie i zapisywanie plików. Można pracować z plikami tekstowymi (`.txt`), binarnymi (`.bin`) i innymi formatami.
### Otwieranie plików (`open`)
Pliki otwieramy za pomocą funkcji `open()`, podając nazwę pliku i tryb otwarcia.

Tryb	|Opis
--|--
`"r"`	|Odczyt (domyślnie)
`"w"`	|Zapis (usuwa zawartość pliku!)
`"a"`	|Dopisanie do pliku
`"x"`	|Tworzy nowy plik (błąd, jeśli istnieje)
`"b"`	|Tryb binarny (np. `"rb"`, `"wb"`)

Przykład – otwieranie pliku do odczytu
```py
plik = open("dane.txt", "r")            # Otwiera plik w trybie odczytu
tekst = plik.read()                     # Odczytuje całą zawartość
print(tekst)
plik.close()                            # Zamyka plik
```
### Odczytywanie pliku
Odczyt całego pliku (`read()`)
```py
with open("dane.txt", "r") as plik:
    zawartosc = plik.read()
    print(zawartosc)
```
Odczyt wiersz po wierszu (`readline()`, `readlines()`)
```py
with open("dane.txt", "r") as plik:
    for linia in plik:
        print(linia.strip())            # Usuwa znaki nowej linii
```
### Zapis do pliku
Tryb `"w"` (nadpisanie pliku)
```py
with open("nowy.txt", "w") as plik:
    plik.write("To jest nowa linia.\n")
```
Tryb `"a"` (dopisywanie)
```py
with open("nowy.txt", "a") as plik:
    plik.write("Dopisuję kolejną linię.\n")
```
### Tryb binarny
Dla plików graficznych, dźwiękowych itp.

Odczyt binarny
```py
with open("obraz.jpg", "rb") as plik:
    dane = plik.read()
```
Zapis binarny
```py
with open("kopiowany.jpg", "wb") as plik:
    plik.write(dane)
```
### Obsługa błędów (`try-except`)
Jeśli plik nie istnieje, program może zgłosić błąd.
```py
try:
    with open("brak.txt", "r") as plik:
        print(plik.read())
except FileNotFoundError:
    print("Plik nie istnieje!")
```
# Moduły i importy w Pythonie
Moduły w Pythonie pozwalają na organizowanie kodu w osobne pliki i ponowne ich użycie w różnych programach. Python ma też wiele wbudowanych modułów, które rozszerzają jego funkcjonalność.

### Importowanie modułów

Moduły importujemy za pomocą `import`.

Import całego modułu
```py
import math

print(math.sqrt(16))    # 4.0
```
Import konkretnej funkcji
```py
from math import sqrt

print(sqrt(25))         # 5.0
```
Import z aliasem (`as`)
```py
import math as m

print(m.pi)             # 3.141592653589793
```
### Tworzenie własnych modułów
Każdy plik `.py` może być modułem!

Plik `moj_modul.py`
```py
def powitanie(imie):
    return f"Cześć, {imie}!"
```
Użycie modułu w innym pliku
```py
import moj_modul

print(moj_modul.powitanie("Ania"))  # Cześć, Ania!
```
### Importowanie wszystkiego (`*`)
```py
from math import *

print(sin(0))           # 0.0
print(factorial(5))     # 120
```
> **Uwaga:** Nie zaleca się `from module import *`, bo może nadpisać inne funkcje o tej samej nazwie.
### Moduł `sys` – Argumenty wiersza poleceń
Moduł `sys` pozwala na odczyt argumentów podanych przy uruchamianiu skryptu.

Przykład (`sys.argv`)
```py
import sys

print("Argumenty:", sys.argv)
```
> Uruchomienie `python skrypt.py argument1 argument2` zwróci:\
> `Argumenty: ['skrypt.py', 'argument1', 'argument2']`
### Moduł `os` – Operacje na plikach i katalogach
Moduł `os` pozwala na zarządzanie plikami i katalogami.

Sprawdzenie plików w katalogu
```py
import os

print(os.listdir("."))              # Lista plików w bieżącym katalogu
```
Sprawdzenie, czy plik istnieje
```py
print(os.path.exists("plik.txt"))   # True / False
```
Tworzenie katalogu
```py
os.mkdir("nowy_folder")
```
Usunięcie pliku
```py
os.remove("plik.txt")
```
### Moduł random – Losowanie liczb
```py
import random

print(random.randint(1, 10))            # Losowa liczba 1-10
print(random.choice(["A", "B", "C"]))   # Losowy element listy
```