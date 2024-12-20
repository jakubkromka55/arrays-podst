# Funkcja tworząca dwuwymiarową tablicę o wymiarach x na y, wypełnioną zerami
def create_2d_arr(x, y):
    return [[0 for _ in range(y)] for _ in range(x)]

# Tworzenie tablicy 3 na 5
arr = create_2d_arr(3, 5)

# Drukowanie tablicy
for row in arr:
    print(row)
