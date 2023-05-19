for test in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int,str(input()))))



    mid = n//2
    sum_arr = 0
    for i in range(n):
        if i <= mid:
            j = i
            
            sum_arr += sum(arr[i][mid-j:mid+j+1])
        else:
            j = n-i-1
            
            sum_arr += sum(arr[i][mid - j:mid + j + 1])


    print('#'+str(test+1), sum_arr)