for test in range(int(input())):

    n, m, k = map(int,input().split())
    consumer = list(map(int,input().split()))
    consumer.sort()
    result = 'Possible'
    for i in range(n):
        boong = (consumer[i]//m)*k - (i+1)#손님 수
        if boong < 0:
            result = 'Impossible'
            break

    print('#'+str(test+1), result)