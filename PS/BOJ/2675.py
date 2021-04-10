#2675 문자열 반복
#https://www.acmicpc.net/problem/2675

t = int(input())

for i in range(t):
    num, s = input().split()
    result=''
    for i in s:
        result += int(num)*i
    print(result)