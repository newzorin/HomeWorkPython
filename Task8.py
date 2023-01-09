import random
my_list = [1, 2, 3, 4, 5]
time = 0
for i in range(len(my_list)):
    a = random.randint(0, len(my_list) - 1)
    my_list[time] = my_list[i]
    my_list[i] = my_list[a]
    my_list[a] = my_list[time]

print(my_list)


    