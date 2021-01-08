
n= 6
arr1 = [46, 33, 33, 22, 31,50]
arr2 = [27, 56, 19, 14, 14, 10]

def solution(arr1, arr2, n):
    result = []
    for i in range (n):
        sol = arr1[i] | arr2[i]
        result.append(bin(sol)[2:].zfill(n).replace('1','#').replace('0', ' '))

    print (result)
solution(arr1, arr2, n)



