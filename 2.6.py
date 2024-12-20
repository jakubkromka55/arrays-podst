# Macierz 3x3 początkowo wypełniona zerami
matrix = [
   [0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]
]

# Zamiana wartości na głównej przekątnej na 1
for i in range(len(matrix)):
    matrix[i][i] = 1  # Zmiana wartości na przekątnej na 1

# Wydrukowanie zmodyfikowanej tablicy
for row in matrix:
    print(" ".join(map(str, row)))  # Drukowanie wiersza z wartościami oddzielonymi spacjami
