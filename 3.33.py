# Inicjalizacja tablicy 3x5 z liczbami całkowitymi
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Funkcja do wyświetlania tablicy
def print_array(arr):
    for row in arr:
        print(" ".join(map(str, row)))

# Wyświetlenie tablicy przed zmianami
print("Tablica przed zmianą:")
print_array(arr)

# Zamiana pierwszej i ostatniej kolumny
for row in arr:
    row[0], row[-1] = row[-1], row[0]

# Wyświetlenie tablicy po zmianach
print("\nTablica po zmianie:")
print_array(arr)
