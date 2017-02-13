for num in range(1, 101, 1):
    if (num % 3 == 0):
        if(num % 5 == 0):
            print("FizzBuzz,",end="")
        else:
            print("Fizz,",end="")
    elif (num % 5 == 0):
        print ("buzz,", end="")
    else:
        print(str(num) + ",", end="")
