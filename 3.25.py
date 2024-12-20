import matplotlib.pyplot as plt

x = []
y = []

# Tworzymy wartości x w zakresie od -100 do 100
for n in range(-100, 101):
    x.append(n)

# Tworzymy wartości y na podstawie funkcji f(x) = x^2 - 3
for n in x:
    y.append(n**2 - 3)

# Rysowanie wykresu
plt.plot(x, y)

# Dodanie tytułu i etykiet osi
plt.title("Wykres funkcji f(x) = x^2 - 3")
plt.xlabel("x")
plt.ylabel("f(x)")

# Wyświetlenie wykresu
plt.show()
