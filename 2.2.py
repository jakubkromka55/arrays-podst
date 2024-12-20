# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

# Drukowanie planszy
for row in tic_tac_toe_board:
    for cell in row:
        print(cell, end=" ")  # Wydrukuj komórkę z przestrzenią na końcu
    print()  # Przejdź do nowej linii po każdym wierszu
