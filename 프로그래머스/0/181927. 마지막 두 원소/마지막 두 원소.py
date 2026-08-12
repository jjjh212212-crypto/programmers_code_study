def solution(num_list):
    a = num_list[-1]-num_list[-2]
    if a > 0:
        num_list.append(a)
    else:
        num_list.append(num_list[-1]*2)
    return num_list