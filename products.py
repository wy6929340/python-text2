products = []


while True:
    name = input("請輸入商品:")
    if name == "q":
        break
    pice = input("請輸入價格:")
    pice = int(pice)
    #p = []
    #p.append(name)
    #p.append(pice)
    #products.append(p)
    products.append([name,pice])
print(products)

for p in products:
    print(p[0],"的價格:", p[1], "元")

with open("products.csv", "w", encoding = "utf-8") as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0] + "," + str(p[1]) + "\n" )


with open("products.csv", "r", encoding = "utf-8") as f:
    for line in f:
        if "商品,價格" in line:
            continue
        name , pice = line.strip().split(",")
        products.append([name,pice])
print(products)