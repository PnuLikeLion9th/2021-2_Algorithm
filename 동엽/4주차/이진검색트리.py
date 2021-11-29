import sys
sys.setrecursionlimit(10**6)


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
preorder = [50,30,24,5,28,45,98,52,60]
def postorder(start,end):
    if start>end: #리프노드일시 종료
        return
    root = preorder[start]
    idx = start+1

    while idx<=end:#분기점 체크
        if preorder[idx]>root:#루트노드보다 큰값이면 오른쪽서브트리
            break
        idx+=1

    postorder(start+1,idx-1)
    postorder(idx,end)
    print(root)


postorder(0,len(preorder)-1)

