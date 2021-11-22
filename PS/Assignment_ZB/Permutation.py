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

print(solution(3,3)) # [2,1,3]
print(solution(4,9)) # [2,3,1,4]


# for문을 이용하여 배열에 삽입 시 다음과 같이 간략하게도 사용 가능함
  #seq = [i for i in range(1,n+1)]
  #perm = list(itertools.permutations(seq))
  #result = [item for item in perm[k-1]]
