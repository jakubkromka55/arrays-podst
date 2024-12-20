# Tablica 2D z liczbami całkowitymi
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Inicjalizacja zmiennych do śledzenia minimalnej i maksymalnej wartości oraz ich pozycji
min_value = arr[0][0]
max_value = arr[0][0]
min_pos = (0, 0)
max_pos = (0, 0)

# Iteracja po wszystkich elementach tablicy
for i in range(len(arr)):
    for j in range(len(arr[i])):
        # Sprawdzanie, czy wartość jest mniejsza niż aktualnie zapisana minimalna
        if arr[i][j] < min_value:
            min_value = arr[i][j]
            min_pos = (i, j)  # Zapisanie pozycji najmniejszej wartości
        # Sprawdzanie, czy wartość jest większa niż aktualnie zapisana maksymalna
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_pos = (i, j)  # Zapisanie pozycji największej wartości

# Drukowanie wyników z informacjami o wierszu i kolumnie (indeksy + 1, bo liczymy od 1)
print(f"Najmniejsza wartość: {min_value} (wiersz: {min_pos[0] + 1}, kolumna: {min_pos[1] + 1})")
print(f"Największa wartość: {max_value} (wiersz: {max_pos[0] + 1}, kolumna: {max_pos[1] + 1})")
