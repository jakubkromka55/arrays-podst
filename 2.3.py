# Miesięczne wydatki w różnych kategoriach dla każdego tygodnia
monthly_expenses = [
   [200, 50, 100],  # Tydzień 1: Żywność, Transport, Media
   [180, 60, 110],  # Tydzień 2
   [220, 55, 105],  # Tydzień 3
   [210, 65, 95]    # Tydzień 4
]

# Zmienne do sumowania wydatków w każdej z kategorii
total_food = 0       # Całkowite wydatki na żywność
total_transport = 0  # Całkowite wydatki na transport
total_utilities = 0  # Całkowite wydatki na media
total_weekly_expenses = []  # Lista do przechowywania wydatków tygodniowych

# Pętla przechodzi przez dane tygodniowe i sumuje wydatki w poszczególnych kategoriach
for week in monthly_expenses:
    total_food += week[0]       # Sumowanie wydatków na żywność
    total_transport += week[1]  # Sumowanie wydatków na transport
    total_utilities += week[2]  # Sumowanie wydatków na media

# Obliczenie wydatków na każdy tydzień, dodając wszystkie kategorie
for week in monthly_expenses:
    total_weekly_expenses.append(sum(week))  # Suma wydatków dla danego tygodnia

# Sumowanie całkowitych wydatków na miesiąc
total_monthly_expenses = sum(total_weekly_expenses)  # Suma wydatków z każdego tygodnia

# Drukowanie wyników: całkowite wydatki dla każdej kategorii
print('MIESIĘCZNE WYDATKI')
print('------------------')
print('Żywność:', total_food)            # Wydatki na żywność
print('Transport:', total_transport)    # Wydatki na transport
print('Media:', total_utilities)        # Wydatki na media

# Drukowanie wydatków na każdy tydzień
for i, weekly_expense in enumerate(total_weekly_expenses, 1):
    print(f'Tydzień {i}:', weekly_expense)  # Całkowite wydatki w danym tygodniu

print('------------------')
print('RAZEM:', total_monthly_expenses)  # Całkowite wydatki za cały miesiąc
