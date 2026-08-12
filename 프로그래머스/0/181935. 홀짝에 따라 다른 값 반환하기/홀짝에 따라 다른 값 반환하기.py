def solution(n):
    if n%2 == 1:
        answer = (n//2+1)**2
    else:
        answer = 0
        for i in range(n//2):
            answer += ((i+1)*2)**2
    return answer