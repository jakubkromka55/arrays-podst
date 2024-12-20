# Funkcja implementująca algorytm Bubble Sort
def bubblesort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:  # Jeśli element jest większy od następnego
                array[j], array[j + 1] = array[j + 1], array[j]  # Zamień miejscami
    return array

# Przykładowe tablice do posortowania
array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 3, 8, 6, 2, 7, 4, 1]
array3 = [15, 8, 31, 47, 2, 19]

# Sortowanie i drukowanie wyników
print("Original array1:", array1)
print("Sorted array1:", bubblesort(array1))

print("nOriginal array2:", array2)
print("Sorted array2:", bubblesort(array2))

print("Original array3:", array3)
print("Sorted array3:", bubblesort(array3))
