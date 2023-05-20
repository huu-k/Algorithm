for test in range(10):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    count = 0
    for i in range(n):#열
        state = 0
        for j in range(n):#행

            if arr[j][i] == 1 and state == 0:
                state = 1
            elif arr[j][i] == 2 and state == 1:
                state = 0
                count+=1



    print('#'+str(test+1), count)