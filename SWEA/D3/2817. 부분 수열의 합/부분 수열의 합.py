from itertools import combinations

for test in range(int(input())):

    n , k = map(int,input().split())

    arr = list(map(int,input().split()))


    result = []

    for i in range(1,n+1):
        for key in combinations(arr,i):

            result.append(sum(key))



    print('#'+str(test+1), result.count(k))