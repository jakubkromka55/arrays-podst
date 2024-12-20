def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # Zmieniamy zakres j, ponieważ po każdym przejściu ostatnie elementy są już posortowane
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Zamiana miejscami
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Przykład użycia:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

sorted_arr = bubbleSort(arr)
print("Sorted array:", sorted_arr)
