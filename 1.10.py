# Wyniki testu studenta
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# Liczba pytań
question_number = len(test_results)

# Liczba poprawnych odpowiedzi
correct_answers = 0
for answer in test_results:
    if answer:
        correct_answers += 1

# Liczba błędnych odpowiedzi
incorrect_answers = question_number - correct_answers

# Procent poprawnych odpowiedzi
correct_percentage = (correct_answers / question_number) * 100

# Drukowanie statystyk
print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers: {:.2f}%'.format(correct_percentage))
