num = [9, 6, 7, 1, 2]
print(num)
print("↓")
for i in range(len(num) - 1):
    for j in range(len(num) - 1 - i):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
print(num)
