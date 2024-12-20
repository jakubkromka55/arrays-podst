# Funkcja znajdująca unikalne elementy w tablicy
def find_unique_elements(array):
    unique_elements = []
    for element in array:
        if array.count(element) == 1:  # Sprawdź, czy element występuje tylko raz
            unique_elements.append(element)
    return unique_elements

# Przykładowa tablica
array = [2, 3, 2, 5, 8, 1, 9, 8]

# Znajdowanie unikalnych elementów
unique_elements = find_unique_elements(array)

# Drukowanie wyników
print("Array:", array)
print("Unique elements:", unique_elements)
