num = int(input())

for i in range(1111, 10000):
    for digin in str(i):
        if digin == "0":
            break
        if num % int(digin) != 0:
            break

    else:
        print(i, end=" ")