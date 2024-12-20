# Ceny 10 produktów w sklepie (w jednostkach waluty)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Liczba dostępnych sztuk każdego produktu
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# Obliczanie całkowitej wartości wszystkich towarów w sklepie
total_value = 0
for i in range(len(product_prices)):
    total_value += product_prices[i] * product_quantities[i]

# Drukowanie całkowitej wartości towarów
print(f"The total value of all products in the store is: {total_value:.2f} currency units")
