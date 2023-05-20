for test in range(int(input())):
    arr = list(input())

    count = arr.count('x')
    if count<=7:
        result = 'YES'
    else:
        result = 'NO'
    print('#'+str(test+1), result)