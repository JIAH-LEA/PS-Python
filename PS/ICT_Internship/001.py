#Hackerrank
#Picking Tickets
#TimeComplexity O(nlogn)

def maxTickets(tickets):

    tickets = sorted(tickets)
    result=0
    current=0
    length = len(tickets)

    for i in range(length-1):
        if tickets[i+1] - tickets[i] <=1:
            current += 1
            if current > result:
                result = current
            else:
                current = 0

    return result+1
