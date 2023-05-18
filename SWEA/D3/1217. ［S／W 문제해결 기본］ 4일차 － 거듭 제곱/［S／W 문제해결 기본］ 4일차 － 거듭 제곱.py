def recur(n, k):
    if k<=0:
        return 1
    return n*recur(n,k-1)

for test in range(10):
    t = int(input())
    n, k = map(int, input().split())

    result = recur(n, k)

    print('#' + str(t), result)