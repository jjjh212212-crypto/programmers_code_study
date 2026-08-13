import math
def solution(signals):
    sum_list=[]
    n=len(signals)
    for i in signals:
        sum_list.append((i[0]+1,i[1],sum(i)))
    lcm_signal=math.lcm(*[sum_list[i][2] for i in range(n)])
    min_start=min([sum_list[i][0] for i in range(n)])
    while min_start <= lcm_signal:
        count=0
        for i in sum_list:
            if (min_start-i[0])%i[2] >= i[1]:
                break        
            count+=1
        if count == n:
            return min_start
        min_start+=1
    return -1