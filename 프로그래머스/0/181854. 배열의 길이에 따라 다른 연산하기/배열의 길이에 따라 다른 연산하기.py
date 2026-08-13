def solution(arr, n):
    if len(arr)%2 == 0:
        k=1
    else:
        k=0
    for i in range(k,len(arr),2):
        arr[i]+=n
    return arr