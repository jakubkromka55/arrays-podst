# Lista liczb, które będziemy podnosić do kwadratu
numbers = [8, 2, 5, 1, 9]

# Pusta lista, do której będziemy dodawać kwadraty liczb
squared_numbers = []

# Pętla, która przechodzi przez każdą liczbę w liście 'numbers'
for number in numbers:
    # Dodajemy kwadrat liczby 'number' do listy 'squared_numbers'
    squared_numbers.append(number * number)

print(numbers)

# Wyświetlamy listę z kwadratami liczb
print(squared_numbers)
