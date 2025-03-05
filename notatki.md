# Podstawowe elementy składni w Pythonie

### Struktura programu

W Pythonie kod jest wykonywany od góry do dołu, a nie ma potrzeby definiowania funkcji main(), jak w C++ czy Java. Jednak konwencjonalnie stosuje się poniższy zapis.
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
x = 10        # int
y = 3.14      # float
z = "Hello"   # str
is_python = True  # bool
```
Można też przypisać wiele wartości na raz.
```py
a, b, c = 1, 2.5, "tekst"
```

Typ | Opis|Przykład
--|--|--|
`int`|Liczby całkowite|`x=42`
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
print(type(x))  # output: <class 'int'>
```

### Konwersja typów

Python pozwala na konwersję między typami.

```py
a = "100"
b = int(a)   # Konwersja na int
c = float(a) # Konwersja na float
d = str(b)   # Konwersja na string
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
print(status)  # "dodatnia"
```

### Pętla `for`

Przydatne podczas iteracji po kolekcjach (`list`, `tuple`, `dict`, `set`, `str`).

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
    break  # Przerywa pętlę
```

### `break` i `continue`

- `break` – przerywa pętlę.
- `continue` – pomija resztę kodu i przechodzi do kolejnej iteracji.
```py
for i in range(10):
    if i == 5:
        break  # Przerywa pętlę, gdy i = 5
    print(i)
```
```py
for i in range(5):
    if i == 2:
        continue  # Pomija i = 2
    print(i)
```