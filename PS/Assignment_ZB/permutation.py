#문제 출처: Leetcode
#문제: n과 k가 주어졌을 때, k번째 섞은 결과(result)를 반환하시오

import itertools 
import math

def solution(n,k):
  n_arr = []
  result=[]
  
  for i in range(1,n+1):
     n_arr.append(i)

  perm = list(itertools.permutations(n_arr))

  for item in perm[k-1]:
    result.append(item)

  return result



print(solution(3,3))
print(solution(4,9))



print(solution(3,3))
print(solution(4,9))
