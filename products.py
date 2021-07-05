products = []

while True:
    name = input("請輸入商品:")
    if name == "q":
        break
    pice = input("請輸入價格:")
    p = []
    p.append(name)
    p.append(pice)
    products.append(p)
print(products)