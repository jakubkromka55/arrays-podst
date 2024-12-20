# Definiujemy dwuwymiarową tablicę o rozmiarze 2x4
array = [
    [1, 2, 3, 4],  # Pierwszy wiersz
    [5, 6, 7, 8]   # Drugi wiersz
]

# Drukowanie tablicy w wierszach
for row in array:
    for element in row:
        print(element, end=" ")  # Wydrukowanie elementu w jednym wierszu
    print()  # Nowa linia po każdym wierszu
