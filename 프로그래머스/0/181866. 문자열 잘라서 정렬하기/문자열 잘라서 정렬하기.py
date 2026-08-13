def solution(myString):
    return list(filter(None,sorted(myString.strip('x').split('x'))))