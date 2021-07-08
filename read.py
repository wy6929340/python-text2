data = []
count = 0
len_total = 0
len_num = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count +=1
        if count % 1000 == 0:
            print(len(data))
#print(data[0]) 


for d in data:
    len_total =len_total + len(d)
    len_num = len_total / len(data)
print(len_num)
new_data = []
for d in data:
    if len(d) < 100:
        new_data.append(d)
print(len(new_data))

good_data = []
for d in data:
    if "good" in d:
        good_data.append(d)
print("一共有", len(good_data), "比留言")

good = [d for d in data if "good" in d ]

print(len(good))

#文字記數
wc = {}

for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1 
        else:
            wc[word] = 1
            
    
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    k = input("請輸入想要查詢的字:")
    if k == "q":
        break
    if k in wc:
        print(k,"出現過", wc[k])
    else:
        print(k, "沒在字典裡")
print("感謝使用")








