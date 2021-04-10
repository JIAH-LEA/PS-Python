#1546 평균
#https://www.acmicpc.net/problem/1546

n = int(input())
score_list = list(map(int, input().split()))
maxi = max(score_list)
result = 0

for i in range(0, n):
    score_list[i] = score_list[i] / maxi * 100
    result = result + score_list[i]

result = result / n
print(result)