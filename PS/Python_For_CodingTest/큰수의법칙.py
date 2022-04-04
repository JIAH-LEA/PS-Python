# Chap03 그리디
# 예제 3-2 큰 수의 법칙
# 시간 제한 1초, 메모리 제한 128MB

# 풀이1) 수학적 접근 (몫과 나머지 이용)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0
data.sort()

set_count = m // (k+1)  # 가장 큰 수 k개와 두 번째 큰수 1개 포함된 set의 개수
set_remain = m % (k+1)  # set를 제외한 나머지 개수 ( 가장 큰 수가 채운다 )

result = data[-1] * ((k * set_count) + set_remain) + data[-2] * set_count

print(result)