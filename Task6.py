num = input("Введите число:  ")
sum = 0

for digit in num:
    if digit.isdigit():
        sum = sum + int(digit)

print(sum)