# Lista popularnych gier komputerowych
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# Sortowanie listy alfabetycznie
computer_games.sort()

# Iteracja za pomocą pętli while i numerowanie listy
index = 0
while index < len(computer_games):
    print(f"{index + 1}. {computer_games[index]}")
    index += 1
