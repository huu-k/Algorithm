for test in range(10):
    n = int(input())
    arr =[]
    max_arr = 0

    for _ in range(100):
        arr.append(list(map(int, input().split())))

    #행 비교
    for i in range(100):
        max_arr = max(max_arr, sum(arr[i]))
    #열 비교
    for i in range(100):
        b = [j[i] for j in arr]
        max_arr = max(max_arr, sum(b))


    #대각선
    sum_arr = 0
    for i in range(100):
        sum_arr+=arr[i][i]
    max_arr = max(max_arr, sum_arr)

    #왼쪽 대각선
    sum_arr = 0
    for i in range(99,-1,-1):
        sum_arr+=arr[i][i]
    max_arr = max(max_arr, sum_arr)

    print('#' + str(n), max_arr)