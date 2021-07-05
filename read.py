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
for d in data:
    len_total =len_total + len(d)
    len_num = len_total / len(data)
print(len_num)
new_data = []
for d in data:
    if len(d) < 100:
        new_data.append(d)
print(len(new_data))
