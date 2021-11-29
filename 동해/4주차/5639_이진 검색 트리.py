import sys

def getPostorder(start, end):
    if start > end:
        return

    root = preorder[start] 
    idx = start + 1

    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1

    getPostorder(start+1, idx-1)  
    getPostorder(idx, end) 
    print(root)
    
preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break
    
getPostorder(0, len(preorder)-1)
