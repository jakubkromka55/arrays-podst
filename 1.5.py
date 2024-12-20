# Program modyfikuje wartości w tablicy
arr = [1, 2, 3, 4, 5]
print("Tablica:", arr)

# Odejmij jeden od pierwszego elementu
arr[0] -= 1
print("Tablica:", arr)

# Zwiększ ostatni element tablicy o 4
arr[len(arr) - 1] += 4
print("Tablica:", arr)

# Pomnóż środkowy element tablicy przez 2
srodkowy_index = len(arr) // 2
arr[srodkowy_index] *= 2
print("Tablica:", arr)
