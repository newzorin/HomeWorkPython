x1 = float(input("Введите первую кординату точки A  "))
y1 = float(input("Введите вторую кординату точки A  "))
x2 = float(input("Введите первую кординату точки B  "))
y2 = float(input("Введите вторую кординату точки B  "))

num = (x2 - x1)** 2 + (y2 - y1)** 2 
res = num ** 0.5
res = round(res, 2)
print(res)
