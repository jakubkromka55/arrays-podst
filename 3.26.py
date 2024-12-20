import matplotlib.pyplot as plt
import numpy as np

# Tworzymy wartości x w zakresie 0 do 360 stopni
x = np.linspace(0, 360, 360)  # 360 punktów z zakresu 0 do 360

# Konwertujemy wartości x na radiany, ponieważ funkcja sin() w numpy oczekuje radianów
x_radians = np.radians(x)

# Obliczamy y = sin(x)
y = np.sin(x_radians)

# Rysowanie wykresu
plt.plot(x, y)

# Dodanie tytułu i etykiet osi
plt.title("Wykres funkcji y = sin(x) dla x w zakresie 0–360 stopni")
plt.xlabel("x (stopnie)")
plt.ylabel("y = sin(x)")

# Wyświetlenie wykresu
plt.grid(True)  # Dodanie siatki
plt.show()
