a = int(input("введите число 1  "))
b = int(input("введите число 2  "))

if a > 0 and b > 0:
    print("первая четверть")

elif a < 0 and b > 0:
    print("вторая четверть")

elif a < 0 and b < 0:
    print("третья четверть")

elif a > 0 and b < 0:
    print("четвертая четверть")    