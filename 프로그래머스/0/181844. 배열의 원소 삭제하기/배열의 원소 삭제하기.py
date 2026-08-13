def solution(arr, delete_list):
    i=0
    while True:
        if arr[i] in delete_list:
            arr.pop(i)
            i-=1
        i+=1
        if i == len(arr):
            break
    return arr