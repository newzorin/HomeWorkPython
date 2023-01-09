def Odd_summa(my_list):
    s = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            s = s + my_list[i]
    print(f"Сумма = {s}")

my_list = [0, 1, 2, 3, 4, 5]
Odd_summa(my_list)
print(F"список:{my_list}")

