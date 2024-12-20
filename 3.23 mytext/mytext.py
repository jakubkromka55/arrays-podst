# MyText.py

# Funkcja zwracająca liczbę słów w tekście
def word_count(text):
    words = text.split()  # Dzielimy tekst na słowa
    return len(words)

# Funkcja zwracająca słowa uporządkowane od najdłuższego do najkrótszego
def words_from_longest(text):
    words = text.split()  # Dzielimy tekst na słowa
    words.sort(key=len, reverse=True)  # Sortujemy słowa po długości (od najdłuższego)
    return words

# Funkcja zwracająca słowa uporządkowane alfabetycznie
def words_alphabetically(text):
    words = text.split()  # Dzielimy tekst na słowa
    words.sort()  # Sortujemy słowa alfabetycznie
    return words
