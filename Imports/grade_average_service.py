def calculate_average(grades):
    if not grades:
        return 0

    sum_of_grades = 0
    for grade in grades.values():
        sum_of_grades += grade
    average = round(sum_of_grades / len(grades), 2)
    print(average)
