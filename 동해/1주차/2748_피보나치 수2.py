n = int(input())

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(n))
# -> 시간초과

fibo = []
for i in range(n+1):
    if i >= 2:
        fibo.append(fibo[i-1] + fibo[i-2])
    else:
        fibo.append(i)
print(fibo[-1])

    