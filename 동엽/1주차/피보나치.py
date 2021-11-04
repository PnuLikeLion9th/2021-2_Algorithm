t = int(input())

for i in range(t):
    n = int(input())
    # zero = [0]*(n+1)
    # zero[0] = 1
    # zero[1] = 0
    # one = [0]*(n+1)
    # one[0] = 0
    # one[1] = 1
    zero = [1,0]
    one = [0,1]
    for j in range(2,n+1):
        zero.append(zero[j-1]+zero[j-2])
        one.append(one[j-1]+one[j-2])
    print(zero[n],one[n])
    


