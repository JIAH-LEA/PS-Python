# Chap03 그리디
# 예제 3-2 큰 수의 법칙
# 시간 제한 1초, 메모리 제한 128MB

# 풀이2) 단순 구현

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
