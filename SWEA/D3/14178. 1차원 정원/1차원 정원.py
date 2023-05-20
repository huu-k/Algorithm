for test in range(int(input())):
    n, d = map(int, input().split())
    k = 1 + 2 * d
    if n % k == 0:
        result = n // k
    else:
        result = n // k + 1

    print('#' + str(test + 1), result)