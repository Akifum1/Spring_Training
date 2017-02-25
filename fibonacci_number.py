num = int(input("何番目までのフィボナッチ数ですか？"))
fibo = list(range(0, num))
for i in range(num):
    if i >= 2:
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    print(fibo[i])
