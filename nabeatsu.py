num = 0
for num in range(1,101,1):
    if (num % 3 == 0):
        print("aho!,",end="")
    elif (num % 10 == 3):
        print("aho!,",end="")
    elif (num //10 == 3):
        print("aho!,",end="")
    else:
        print(str(num) + ",",end="")
