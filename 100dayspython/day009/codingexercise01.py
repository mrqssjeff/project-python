students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for key in students_scores:
    score = students_scores[key]
    if 91 <= score <= 100:
        students_scores[key] = "Outstanding"
    elif 81 <= score <= 90:
        students_scores[key] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        students_scores[key] = "Acceptable"
    elif score < 70:
        students_scores[key] = "Fail"
    print(f"{key}: ", end="")
    print(f"{students_scores[key]}")
