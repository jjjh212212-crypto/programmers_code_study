def solution(myString, pat):
    a=''
    for i in pat:
        if i == 'A':
            a+='B'
        else:
            a+='A'
    return int(a in myString)