def findFib(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return findFib(index-1) + findFib(index-2)


n = int(input("Введите число: "))
lst = [findFib(i) for i in range(1, n+2)]
lst = lst[::-1] + lst[1:]
print(lst, '\n')