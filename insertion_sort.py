num = [9, 6, 7, 1, 2]
for i in range(0, len(num) - 1):
    j = i
    while j >= 0 and num[j] > num[j + 1]:
        num[j], num[j + 1] = num[j + 1], num[j]
        j = j - 1
print(num)
