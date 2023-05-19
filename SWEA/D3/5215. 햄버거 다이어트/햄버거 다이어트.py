for test in range(int(input())):
    n, l = map(int, input().split())

        # 칼로리 비교 arr
    arr = [0 for _ in range(l + 1)]
    
    for i in range(n):
        t, k = map(int, input().split())
    
        # 최대 칼로리부터 k 까지 비교
        for j in range(l, k + 1, -1):
            arr[j] = max(arr[j - k] + t, arr[j])
    
    print('#' + str(test + 1), arr[l])