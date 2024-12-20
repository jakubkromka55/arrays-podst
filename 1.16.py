# Sortowanie danych w porządku rosnącym (od najmniejszej do największej)
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
sorted_distances = sorted(distances_traveled)
print("Sorted distances (ascending):", sorted_distances)

# Sortowanie danych w porządku malejącym (od największej do najmniejszej)
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
sorted_temperatures_descending = sorted(daily_temperatures, reverse=True)
print("Sorted temperatures (descending):", sorted_temperatures_descending)

# Sortowanie danych w porządku rosnącym (alfabetycznie)
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
sorted_file_names = sorted(file_names)
print("Sorted file names (ascending):", sorted_file_names)
