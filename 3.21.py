# Funkcja sprawdzająca, czy pierwsza tablica jest podzbiorem drugiej
def is_subset(arr1, arr2):
    # Sprawdzamy, czy wszystkie elementy arr1 są w arr2
    for item in arr1:
        if item not in arr2:
            return False
    return True

# Przykładowe tablice
arr1 = [2, 5, 8]
arr2 = [8, 5, 2, 7, 10, 3]

# Sprawdzamy, czy arr1 jest podzbiorem arr2
if is_subset(arr1, arr2):
    print(f"Tablica {arr1} jest podzbiorem tablicy {arr2}")
else:
    print(f"Tablica {arr1} nie jest podzbiorem tablicy {arr2}")
