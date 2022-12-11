judjes_count = int(input())

total_greads = 0
total_grades_sum = 0

while True:
    name = input()
    if name == "Finish":
        break
    grade_sum = 0

    for i in range(judjes_count):
        grade_sum += float(input())

        total_grades_sum += grade_sum
        total_greads += judjes_count
        print(f"{name} - {grade_sum / judjes_count:.2f}.")
        mark_sum = 0

print(f"Student's final assessment is {(total_grades_sum / total_greads):.2f}.")