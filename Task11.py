
def Product_of_par(my_list):
    l = len(my_list) // 2 + 1 if len(my_list) % 2 != 0 else len(my_list)//2
    new_lst = [my_list[i]*my_list[len(my_list)-i-1] for i in range(l)]
    print(new_lst)


my_list = [2, 3, 4, 5, 6]
Product_of_par(my_list)

