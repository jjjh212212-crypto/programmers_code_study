def solution(ineq, eq, n, m):
    if eq == '!':
        return int(eval(f'{n}'+ineq+f'{m}'))
    return int(eval(f'{n}'+ineq+eq+f'{m}'))