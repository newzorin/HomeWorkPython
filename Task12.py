lst = [1.1, 1.2, 3.1, 5, 10.01]
new_lst = [round(i % 1,2) for i in lst if i % 1 != 0]
print(max(new_lst) - min(new_lst))


