# Funkcja konwertująca tablicę dwuwymiarową na jednowymiarową
def convert_to_1d(matrix):
    result = []
    for row in matrix:
        result.extend(row)  # Rozszerzamy wynik o elementy wiersza
    return result

# Przykładowe tablice dwuwymiarowe
matrix1 = [
    [2, 3],
    [1, 5]
]

matrix2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

matrix3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# Drukowanie jednowymiarowych tablic dla każdej z macierzy
for idx, matrix in enumerate([matrix1, matrix2, matrix3], start=1):
    one_d_array = convert_to_1d(matrix)
    print(f"Jednowymiarowa tablica {idx}: {one_d_array}")
