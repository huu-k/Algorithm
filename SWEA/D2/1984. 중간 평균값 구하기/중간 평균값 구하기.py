import heapq

test_case = int(input())

for i in range(test_case):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.remove(arr[0])
    arr.remove(arr[-1])
    print('#'+str(i+1), round(sum(arr)/len(arr)))