def solution(str_list, ex):
    str=''
    for i in str_list:
        if ex not in i:
            str+=i
    return str