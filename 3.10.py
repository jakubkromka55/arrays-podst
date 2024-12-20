# Tablice wejściowe
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

# Funkcja zwracająca elementy z array1, które nie występują w array2
def find_unique_elements(arr1, arr2):
    result = []
    for num in arr1:
        if num not in arr2:  # Sprawdzanie, czy liczba nie występuje w drugiej tablicy
            result.append(num)
    return result

# Wywołanie funkcji i wydrukowanie wyniku
unique_elements = find_unique_elements(array1, array2)
print(unique_elements)
