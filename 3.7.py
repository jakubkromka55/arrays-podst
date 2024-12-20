# Tablica z nazwami
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# Zmienna do przechowywania najdłuższej nazwy
longest_name = ""

# Iteracja po każdej nazwie w tablicy
for name in names:
    # Sprawdzamy, czy aktualna nazwa jest dłuższa od dotychczasowej najdłuższej
    if len(name) > len(longest_name):
        longest_name = name

# Drukujemy wyniki
print("Names:", " ".join(names))
print("Longest name:", longest_name)
