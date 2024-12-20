# Tablica z liczbami
numbers = [-15, 8, -31, 47, -2, 19]

# Inicjalizujemy zmienne dla maksymalnej i minimalnej liczby
max_num = numbers[0]
min_num = numbers[0]

# Przechodzimy po tablicy i porównujemy każdą liczbę
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Drukowanie wyników
print("Maximum number:", max_num)
print("Minimum number:", min_num)
