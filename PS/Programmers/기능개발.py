#스택,큐 Level2

def solution(progresses, speeds):
    progresses = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    answer = []
    maximum=progresses[0]
    touch=0
    count=0
    print(progresses)

    for i in range(len(progresses)):
        if(progresses[i]>maximum):
            answer.append(count)
            count=1
            maximum=progresses[i]
        else:
            count+=1
        if(i==len(progresses)-1):
            answer.append(count)
    return answer
