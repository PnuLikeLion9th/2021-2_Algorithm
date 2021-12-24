n = int(input())
if n<100:
    print(n)
elif n==1000:
    print(144)
else:
    cnt = 99
    for i in range(100,n+1):
        a,b,c = str(i)
        if int(b)-int(a) == int(c)-int(b):
            cnt+=1

    print(cnt)