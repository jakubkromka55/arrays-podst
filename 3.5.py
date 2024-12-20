# Tablica z wartościami
numbers = [15, 8, 31, 47, 2, 19]

# Zmienna do sumowania wartości
total = 0

# Obliczamy sumę wartości w tablicy
for num in numbers:
    total += num

# Obliczamy średnią arytmetyczną
average = total / len(numbers)

# Drukujemy wyniki
print("Array:", numbers)
print("Average:", average)
