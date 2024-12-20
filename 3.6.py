# Tablica z wartościami
numbers = [15, 8, 31, 47, 2, 19]

# Zmienna do sumowania wartości
total = 0

# Indeks początkowy
i = 0

# Obliczamy sumę wartości w tablicy za pomocą pętli while
while i < len(numbers):
    total += numbers[i]
    i += 1

# Obliczamy średnią arytmetyczną
average = total / len(numbers)

# Drukujemy wyniki
print("Array:", numbers)
print("Average:", average)
