# 프로그래머스_모의고사_브루트포스_레벨 1 

numbers = [[1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 
            [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5], 
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
answers = [1,3,2,4,2]

def solution(answers, numbers):
    answer = []
    solution_sum = 0
    i = 0
    j = 0
    k = 0
    while 1:
        if j == 3:
            break

        if answers[i] == numbers[j][k]:
            solution_sum += 1
        i += 1
        k += 1

        if (j == 0 and k == 10) or (j == 1 and k == 16) or (j == 2 and k == 20):
            k = 0

        if i == len(answers):
            answer.append(solution_sum)
            j += 1
            k = 0
            i = 0
            solution_sum = 0

        
    
    answer_max = max(answer)
    index = []

    for i in range(3):
        if answer_max == answer[i]:
            index.append(i+1)
    
    return index

print(solution(answers, numbers))        



