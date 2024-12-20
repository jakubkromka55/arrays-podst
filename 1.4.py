# Program drukuje informacje o tablicy
arr = [2, 3, 7, 5, 4]

print("Tablica:", arr)

print("Liczba elementów:", len(arr))
print("Pierwsza wartość:", arr[0])
print("Druga wartość:", arr[1])
print("Ostatnia wartość:", arr[len(arr) - 1])
print("Przedostatnia wartość:", arr[len(arr) - 2])

# Suma pierwszej i ostatniej wartości
print("Suma pierwszej i ostatniej wartości:", arr[0] + arr[len(arr) - 1])

# Wartość średnia
print("Wartość średnia:", sum(arr) / len(arr))

# Wyświetlenie wszystkich wartości tablicy
print("Wszystkie wartości tablicy:", end=" ")
for val in arr:
    print(val, end=" ")
print()
