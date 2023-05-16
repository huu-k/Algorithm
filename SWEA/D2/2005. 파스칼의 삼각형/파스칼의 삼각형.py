for test in range(int(input())):
    arr = []
    n = int(input())
    for i in range(0,n+1):
        arr.append(list())
        for j in range(0, i):
            if j == 0:
                arr[i].append(1)
            elif j == i-1:
                arr[i].append(1)
            else:
                arr[i].append(arr[i-1][j-1]+arr[i-1][j])
    print('#' + str(test + 1))

    for k in range(1,n+1):
        for m in range(k):
            print(arr[k][m], end = ' ')
        print()