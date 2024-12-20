# Funkcja zliczająca elementy większe od podanej wartości
def count_greater_than(value, arr):
    count = 0
    for num in arr:
        if num > value:
            count += 1
    return count

# Przykładowa tablica liczb rzeczywistych
arr = [1, 2, 3, 4, 5, 6]

# Pobieramy wartość od użytkownika
value = float(input("Podaj wartość: "))

# Wywołujemy funkcję i wypisujemy wynik
count = count_greater_than(value, arr)
print(f"Liczba elementów większych od {value}: {count}")
