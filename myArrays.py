# Moduł myArrays

# Funkcja zwracająca drugi co do wielkości element tablicy
def second_largest(arr):
    unique_arr = list(set(arr))  # Usuwamy duplikaty
    unique_arr.sort()  # Sortujemy tablicę
    if len(unique_arr) < 2:
        return None  # Jeśli nie ma drugiego co do wielkości elementu
    return unique_arr[-2]

# Funkcja zwracająca medianę
def median(arr):
    arr.sort()  # Sortujemy tablicę
    n = len(arr)
    if n == 0:
        return None
    if n % 2 == 1:
        return arr[n // 2]  # Środkowy element dla nieparzystej liczby elementów
    else:
        # Średnia dwóch środkowych elementów dla parzystej liczby elementów
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

# Funkcja zwracająca najmniejszy i największy element
def min_max(arr):
    if not arr:
        return None, None  # Zwracamy None, jeśli tablica jest pusta
    return min(arr), max(arr)  # Zwracamy najmniejszy i największy element

# Funkcja zwracająca elementy tablicy jako łańcuch znaków
def numbers_as_string(arr):
    return ", ".join(map(str, arr))  # Łączenie elementów w jeden ciąg znaków
