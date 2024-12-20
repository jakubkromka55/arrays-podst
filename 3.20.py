# Funkcja oddzielająca liczby parzyste od nieparzystych
def separate_even_odd(arr):
    even = []
    odd = []
    
    # Przechodzimy przez tablicę i dzielimy liczby na parzyste i nieparzyste
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    # Łączymy tablicę parzystych i nieparzystych liczb
    return even + odd

# Przykładowa tablica liczb całkowitych
arr = [7, 9, 2, 4, 5, 6]

# Oddzielamy liczby parzyste i nieparzyste
arr = separate_even_odd(arr)

# Drukujemy wynik
print("arr =", arr)
