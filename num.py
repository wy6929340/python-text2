import random
start = input("請輸入起始數字:")
end = input("請輸入結束數字:")
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    count+=1
    num = input("請輸入數字:")
    num = int(num)
    if num > end or num < start:
        print("數字超過範圍 請重新輸入")
    else:       
        print("你猜了", count, "次")
        if num == r:
        
            print("猜對了")
            break
        else:
            print("猜錯了")
            if num > r:
                print("比答案大")
            else:
                print("比答案小")
