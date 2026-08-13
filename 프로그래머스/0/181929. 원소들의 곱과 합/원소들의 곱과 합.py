def solution(num_list):
    k=1
    return int(sum(num_list)**2 > [k := k*i for i in num_list][-1])