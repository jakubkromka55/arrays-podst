# Funkcja sprawdzająca, czy dana liczba znajduje się w tablicy
def occurs(number, array):
    # Przechodzimy przez każdy element w tablicy
    for i in array:
        # Jeśli znajdziemy liczbę równą podanej, zwracamy True
        if i == number:
            return True
    
    return False

# Przykładowa tablica liczb
arr = [15, 38, 7, 23, 14]

# Pobranie liczby od użytkownika
nr = int(input("Podaj numer: "))

# Drukowanie wyniku działania funkcji occurs
print(f"{nr} appears in the array: {occurs(nr, arr)}")
