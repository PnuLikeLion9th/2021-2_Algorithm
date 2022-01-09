# 백준_5639_이진 검색 트리_트리_실버 1

import sys
input = sys.stdin.readline

nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

parent = [-1]*max(nums)
lc = [-1]*max(nums)
rc = [-1]*max(nums)

for i in range(1, len(nums)):
    if nums[i] > nums[0]:  # 오른
        if nums[i] > nums[i-1]:

    else:  # 왼
        if nums[i] > nums[i-1]:
            if nums[i-1] < parent[nums[i-1]] < nums[i]:
                parent[nums[i]] = parent[nums[i-1]]
                rc[parent[nums[i-1]]] = nums[i]

        else:
            parent[nums[i]] = nums[i-1]
            lc[nums[i-1]] = nums[i]
