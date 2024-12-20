# Funkcja porównująca dwie tablice
# Zwraca True, jeśli tablice mają taką samą długość i identyczne elementy w tych samych pozycjach
def compare(array1, array2):
    # Sprawdzenie, czy tablice mają różne długości
    if len(array1) != len(array2): 
        return False
    # Pętla sprawdzająca, czy wszystkie elementy są takie same
    i = 0
    while i < len(array1):
        if array1[i] != array2[i]:  # Porównanie elementów w tej samej pozycji
            return False
        i += 1  # Przejście do następnego elementu
    return True  # Tablice są takie same

# Przykładowe tablice do porównania
arr1 = ["water", "book", "sky"]
arr2 = ["water", "book", "sky"]

arr3 = [True, False]
arr4 = [True, False, True]

arr5 = [5, 3, 1]
arr6 = [5, 3, 1]

arr7 = [3, 2, 1]
arr8 = [3, 2]

# Porównanie tablic i wydrukowanie wyników
print(f'Array1: {arr1}\nArray2: {arr2}\nArrays are the same: {compare(arr1, arr2)}')
print(f'Array1: {arr3}\nArray2: {arr4}\nArrays are the same: {compare(arr3, arr4)}')
print(f'Array1: {arr5}\nArray2: {arr6}\nArrays are the same: {compare(arr5, arr6)}')
print(f'Array1: {arr7}\nArray2: {arr8}\nArrays are the same: {compare(arr7, arr8)}')
