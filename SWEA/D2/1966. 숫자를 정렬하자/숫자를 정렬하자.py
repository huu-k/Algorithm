
test_case = int(input())

for i in range(test_case):
    len_n = int(input())

    arr = list(map(int,input().split()))
    arr.sort()
    print('#'+str(i+1), end=' ')

    for j in range(len(arr)):
        print(arr[j], end=' ')
    print()
