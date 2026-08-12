def solution(num_list, n):
    b = (len(num_list)-1)//n 
    return [num_list[n*i] for i in range(b+1)]