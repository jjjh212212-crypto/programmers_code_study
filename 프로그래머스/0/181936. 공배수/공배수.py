def solution(number, n, m):
    k=n*m
    while m > 0:
        n, m = m, n % m
    return 1 if number%(k//n) == 0 else 0