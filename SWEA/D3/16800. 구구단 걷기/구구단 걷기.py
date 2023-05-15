import heapq


test_case = int(input())
for test in range(test_case):
    arr = []
    n = int(input())
    
    print('#'+str(test+1), end=' ')
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            heapq.heappush(arr, (i + n//i))
    if not arr:
        print(n-2)
    else:
        print(heapq.heappop(arr)-2)
    