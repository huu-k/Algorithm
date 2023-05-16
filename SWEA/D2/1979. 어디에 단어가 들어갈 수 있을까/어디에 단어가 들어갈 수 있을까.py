for test in range(int(input())):
    n , k = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    result = 0
    #가로
    for i in range(n):
        count = 0
        for j in range(n):

            if arr[i][j] == 1:
                count+=1
            if arr[i][j] == 0 or j== n-1:

                if count == k:
                    result+=1
                count = 0
    #세로
    for i in range(n):
        count = 0
        for j in range(n):

            if arr[j][i] == 1:
                count+=1
            if arr[j][i] == 0 or j== n-1:

                if count == k:
                    result+=1
                count = 0

    print('#' + str(test + 1), result)
