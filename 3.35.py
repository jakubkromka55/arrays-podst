# Funkcja do transponowania macierzy
def transpose_matrix(m):
    # Tworzymy nową macierz transponowaną, zamieniając wiersze na kolumny
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# Funkcja do drukowania macierzy
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Podane macierze
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [
    [5, 6, 7, 8]
]

# Drukowanie macierzy i ich transpozycji
for idx, matrix in enumerate([matrix1, matrix2, matrix3], start=1):
    print(f"\nMacierz {idx}:")
    print_matrix(matrix)
    transposed = transpose_matrix(matrix)
    print(f"\nTransponowana macierz {idx}:")
    print_matrix(transposed)
