# Importujemy nasz moduł myArrays
import myArrays

# Przykładowa tablica
arr = [7, 3, 8, 5, 2]

# Drukujemy różne informacje o tablicy
print("Numbers:", myArrays.numbers_as_string(arr))  # Wyświetlamy tablicę jako ciąg znaków

# Wyświetlamy drugi co do wielkości element
print("Second largest number:", myArrays.second_largest(arr))

# Wyświetlamy medianę
print("Median:", myArrays.median(arr))

# Wyświetlamy najmniejszy i największy element
min_num, max_num = myArrays.min_max(arr)
print("Smallest and largest number:", min_num, max_num)
