# Wyniki pomiarów temperatury w marcu
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# Liczba pomiarów
measurements = len(temperatures)

# Obliczanie średniej temperatury
temp_total = 0
for temp in temperatures:
    temp_total += temp
avg_temp = temp_total / measurements

# Obliczanie minimalnej i maksymalnej temperatury
min_temp = min(temperatures)
max_temp = max(temperatures)

# Obliczanie liczby dni z temperaturą ujemną
negative_temp = 0
i = 0
while i < measurements:
    if temperatures[i] < 0:
        negative_temp += 1
    i += 1

# Drukowanie raportu
print('TEMPERATURE REPORT')
print('==================')
print('Month: March')
print('Number of measurements:', measurements)
print('Average temperature in the month: {:.2f}'.format(avg_temp))
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of days with negative temperature:', negative_temp)
