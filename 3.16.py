# Tworzymy krotkę, która zawiera różne typy danych
my_tuple = ("Siedem", [10, 20, 30], (5, 15, 25))

# Wypisujemy pierwszy element krotki, który jest łańcuchem tekstowym "Siedem"
print(my_tuple[0])

# Wypisujemy ostatni element listy znajdującej się w drugim elemencie krotki
# my_tuple[1] to lista [10, 20, 30], a my_tuple[1][-1] zwraca ostatni element tej listy, czyli 30
print(my_tuple[1][-1])
