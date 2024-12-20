# Zwraca nazwę dnia tygodnia dla podanego numeru dnia (1-Poniedziałek ... 7-Niedziela)
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= n <= 7:
        return weekdays[n - 1]
    else:
        return "Invalid day number"

# Drukujemy nazwę dnia tygodnia dla numerów 1, 4 i 7
for day in [1, 4, 7]:
    print(f"Dzień {day}: {weekday(day)}")
