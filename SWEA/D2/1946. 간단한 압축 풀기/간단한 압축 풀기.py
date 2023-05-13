test_case = int(input())

for i in range(test_case):
    n = int(input())
    arr = []
    for j in range(n):
        a, b = input().split()
        for _ in range(int(b)):
            arr.append(a)

    print('#'+str(i+1))
    for k in range(0, len(arr), 10):
        for t in range(k, k+10):
            if(t<len(arr)):
        	    print(arr[t], end='')
            else:
                break
        print()
