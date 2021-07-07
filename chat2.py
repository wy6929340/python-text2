def read_file(file_name):
    lines = []
    with open(file_name, "r", encoding = "utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    
    person = None
    allen_sum = 0
    viki_sum = 0 
    allen_s_sum = 0
    viki_s_sum = 0
    allen_image_sum = 0
    viki_image_sum = 0
    
    for line in lines:
        s = line.split(" ")
        name = s[1]
        time = s[0]
        if name == "Allen":
            if s[2] == "貼圖":
                allen_s_sum += 1
            elif s[2] == "圖片":
                allen_image_sum += 1
            else:
                for m in s[2:]:
                    allen_sum += len(m)
        elif name == "Viki":
            if s[2] == "貼圖":
                viki_s_sum += 1
            elif s[2] == "圖片":
                viki_image_sum += 1
            else:
                for m in s[2:]:
                    viki_sum += len(m) 
    print("allen說了", allen_sum, "字")
    print("viki說了", viki_sum, "字")
    print("allen傳了", allen_s_sum, "張貼圖")
    print("viki傳了", viki_s_sum, "張貼圖")
    print("allen傳了", allen_image_sum, "張圖片")
    print("viki傳了", viki_image_sum, "張圖片")
    

def write_file(file_name, lines):
    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")


def main():
    lines = read_file("LINE-Viki.txt")
    lines = convert(lines)
    #write_file("output.txt", lines)
    
main()


