#Hackerrank
#University Career Fair


# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arrival
#  2. INTEGER_ARRAY duration



def maxEvents(arrival, duration):
    num = len(arrival)
    events = []
    if num <= 1: return num
    for i in range(num):
        events.append([arrival[i], duration[i]+arrival[i]])
    events.sort(key=lambda x: x[1])
    cnt = 1
    start = events[0][1]
    for i in range(1,num):
        if start <= events[i][0]:
            cnt+=1
            start = events[i][1]
    return cnt
