for test in range(int(input())):

    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    #90도
    arr_90 = []

    for i in range(n):
        arr90 = ''
        for j in range(n-1,-1,-1):
            arr90+=str(arr[j][i])

        arr_90.append(arr90)

    #180도
    arr_180 = []
    for i in range(n-1,-1,-1):
        arr180 = ''
        for j in range(n-1,-1,-1):
            arr180+=str(arr[i][j])

        arr_180.append(arr180)


    #270도
    arr_270 = []
    for i in range(n - 1, -1, -1):
        arr270 = ''
        for j in range(n):
            arr270 += str(arr[j][i])

        arr_270.append(arr270)

    print('#'+str(test+1))
    for k in range(n):
        print(arr_90[k], arr_180[k], arr_270[k])
