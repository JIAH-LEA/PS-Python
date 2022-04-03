# Chap03 그리디
# 예제 3-1 거스름돈
# 시간복잡도 O(K), k: 화폐의 종류

N = int(input())
coins = [500, 100, 50, 10]
count = 0

for coin in coins:
    count += N // coin
    N %= coin

print(count)
