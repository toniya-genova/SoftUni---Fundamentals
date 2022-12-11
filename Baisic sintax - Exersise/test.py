first_num = int(input())
second_num = int(input())
third_num = int(input())

first_try = ""
second_try = ""
third_try = ""

for i in range(1, first_num + 1):
    if i % 2 == 0:
        first_try = i
    else:
        continue

    for y in range(1, second_num + 1):
        if y >= 2 and y <= 7 and y != 4 and y != 6:
            second_try = y
        else:
            continue

        for e in range(1, third_num + 1):
            if e % 2 == 0:
                third_try = e
                print(f"{first_try} {second_try} {third_try}")
                continue
            else:
                continue