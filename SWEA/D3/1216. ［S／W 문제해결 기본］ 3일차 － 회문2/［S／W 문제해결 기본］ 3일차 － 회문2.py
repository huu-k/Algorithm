for _ in range(10):
    n = int(input())
    arr = [list(input()) for _ in range(100)]

    

    max_arr = 0

    #가로
    for k in range(100, 2, -1):
        for i in range(100):
            for j in range(100-k+1):
                new_arr = arr[i][j:j+k]
                if new_arr == new_arr[::-1]:
                    max_arr = max(max_arr, k)

    #세로
    for k in range(100, 2, -1):
        for i in range(100):#열
            for j in range(100-k+1):#행
                new_arr = [a[i] for a in arr[j:j+k]]
                if new_arr == new_arr[::-1]:
                    max_arr = max(max_arr, k)

    print('#'+str(n), max_arr)
