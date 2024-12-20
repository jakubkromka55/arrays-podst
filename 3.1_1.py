# Tablica z liczbami całkowitymi
numbers = [34, 7, 19, 4, 21, 8]

# Zmienna do przechowywania liczby parzystych liczb
even_count = 0

# Indeksowanie elementów w tablicy za pomocą pętli while
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:  # Sprawdzenie, czy liczba jest parzysta
        even_count += 1  # Zwiększ licznik parzystych liczb
    i += 1  # Przejście do następnego elementu w tablicy

# Drukowanie wyniku
print("Liczba parzystych liczb w tablicy:", even_count)
