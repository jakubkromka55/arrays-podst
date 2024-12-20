# Inicjalizacja dwuwymiarowej tablicy 5x5 wypełnionej zerami
arr = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]  

# Zewnętrzna pętla dla wierszy (od 0 do 4)
for i in range(5):  
    # Wewnętrzna pętla dla kolumn (od 0 do 4)
    for j in range(5):  
        # Wypełnianie tablicy mnożeniem indeksów wiersza i kolumny
        arr[i][j] = (i + 1) * (j + 1)   # Dodanie 1, aby zaczynać od 1 (a nie od 0)

for row in arr:
    # Zastosowanie mapy, aby przekonwertować liczby na stringi
    # Następnie dołączenie ich z pojedynczymi spacjami pomiędzy
    print(" ".join(map(str, row)))
