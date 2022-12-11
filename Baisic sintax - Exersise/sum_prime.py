osum_of_prime_num, sum_of_non_prime_num = 0, 0

while True:
    command = input()

    if command == "stop":
        break

    current_num = int(command)
    is_prime = True

    if current_num < 0:
        print("Number is negative.")
        continue

    for number in range(2, current_num):
        if current_num % 2 == 0:
            is_prime = False
            break
    if is_prime:
        osum_of_prime_num += current_num
    else:
        sum_of_non_prime_num += current_num

print(f"Sum of all prime numbers is: {osum_of_prime_num}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_num}")
