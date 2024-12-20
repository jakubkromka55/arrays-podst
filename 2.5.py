# Układ miejsc w kinie
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Funkcja obliczająca łączną liczbę miejsc
def seats_total(seats):
   return len(seats) * len(seats[0])

# Funkcja obliczająca liczbę dostępnych miejsc
def seats_available(seats):
   available = 0
   for row in seats:
      available += row.count('A')  # Zliczanie dostępnych miejsc (A)
   return available

# Funkcja obliczająca liczbę zarezerwowanych miejsc
def seats_booked(seats):
   booked = 0
   for row in seats:
      booked += row.count('B')  # Zliczanie zarezerwowanych miejsc (B)
   return booked

# Funkcja sprawdzająca status miejsca (dostępne/zarezerwowane)
def seat_status(seats, row, place):
   if seats[row-1][place-1] == 'A':
      return 'Available'
   else:
      return 'Booked'

# Drukowanie informacji o kinie
print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
