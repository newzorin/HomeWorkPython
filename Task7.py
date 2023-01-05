n = int(input("Введите число:  "))

my_list = []
for i in range(1, n+1):
    my_list.append(round((1+1/i)**i, 2))

print(*my_list, sep=", ")
print(sum(my_list))