# Kategorie wydatków i odpowiadające im wydatki
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Znalezienie indeksu największego wydatku
max_expense_index = expenses.index(max(expenses))

# Drukowanie najdroższej kategorii i jej wydatków
print(f"The most expensive category is {categories[max_expense_index]} with an expense of {expenses[max_expense_index]}")
