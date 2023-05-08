
import sys
n = int(input())


a = list(map(int, input().split()))

a.sort()


m = int(input())

b =list(map(int, input().split()))


result = [0]*m

#이진 탐색
def binary_search(arr, target, start, end):

    if start > end:
        return 0

    mid = (start + end)//2

    #성공시 count
    if arr[mid] == target:
        return 1

    if arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)

for i in range(m):
    result[i] = binary_search(a, b[i],0, n-1)


for x in result:
    print(x)






