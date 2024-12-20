# Funkcja do tworzenia macierzy jednostkowej o zadanym rozmiarze
def identity_matrix(size):
    # Tworzymy początkową macierz wypełnioną zerami o wymiarach size x size
    matrix = [[0] * size for _ in range(size)]
    
    # Wstawiamy 1 na przekątną (gdzie indeksy wiersza i kolumny są takie same)
    for i in range(size):
        matrix[i][i] = 1
    
    return matrix

# Funkcja do drukowania macierzy w wierszach i kolumnach
def print_matrix(matrix):
    for row in matrix:
        # Łączymy elementy wiersza w jeden ciąg i wypisujemy je
        print(" ".join(map(str, row)))

# Tworzenie i wyświetlanie macierzy jednostkowych o rozmiarach 3x3, 5x5 i 8x8
for size in [3, 5, 8]:
    print(f"\nMacierz jednostkowa o wymiarze {size}x{size}:")
    # Tworzymy macierz jednostkową o zadanym rozmiarze
    identity = identity_matrix(size)
    
    print_matrix(identity)
