import sys 

def solution(n): 

    num_list = list() 

    for _ in range(n): 
         num_list.append(int(sys.stdin.readline().strip())) 
     
    max_num = max(num_list) 

    print(max_num) 
    print(num_list.index(max_num) + 1) 

