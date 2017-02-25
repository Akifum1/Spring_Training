num = 0
for num in range(1, 151):
    if (num % 3 == 0): #３の倍数
        print("aho!")
    elif "3" in str(num):
        print("aho!")
    else:
        print(str(num))
