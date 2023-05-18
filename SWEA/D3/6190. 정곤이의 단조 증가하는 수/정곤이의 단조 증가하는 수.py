for test in range(int(input())):
    n = int(input())#len(arr
    arr = list(map(int,input().split()))
    new_arr = []
    max_arr = 0

    for i in range(n):
        for j in range(i+1,n):
            new_arr.append(arr[i]*arr[j])

    

    for j in range(len(new_arr)):

        new_x = list(str(new_arr[j]))
        
        for i in range(len(new_x)-1):
            if new_x[i]>new_x[i+1]:
                new_arr[j]=-1
    print('#'+str(test+1), max(new_arr))