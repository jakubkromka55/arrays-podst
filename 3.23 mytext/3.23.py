# Program korzystający z modułu MyText

import mytext  # Importujemy moduł MyText

# Przykładowy tekst
text = "Jedno jabłko dziennie trzyma lekarza z daleka"

# Wywołanie funkcji i drukowanie wyników
print("Text:", text)
print("Number of words:", mytext.word_count(text))
print("Words from the longest:", ", ".join(mytext.words_from_longest(text)))
print("Words ordered alphabetically:", ", ".join(mytext.words_alphabetically(text)))
