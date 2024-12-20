import random

# Funkcja losująca element z tablicy
def rand_elem(array):
    return random.choice(array)

# Przykładowa tablica
arr = [10, 20, 30, 40, 50, 60]

# Wydrukowanie kilku losowych elementów z tablicy
print("Losowe elementy z tablicy:")
for _ in range(5):  # Zmieniaj liczbę iteracji, aby wydrukować więcej losowych elementów
    print(rand_elem(arr))
