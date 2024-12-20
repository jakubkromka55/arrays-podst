# Funkcja zwracająca ciąg gwiazdek o długości n
def star(n):
    return '*' * n

# Tablica z liczbami całkowitymi
numbers = [2, 6, 4, 9, 7]

# Pętla iterująca po elementach tablicy
for number in numbers:
    print(f"{number}: {star(number)}")
