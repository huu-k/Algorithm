import heapq

for test in range(int(input())):

    n = int(input())
    arr = []
    q = []
    break_t = False
    result = 'no'

    for _ in range(n):
        arr.append(list(input()))

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                heapq.heappush(q,[i,j])

    com = False

    for l in range(1,n+1):
        if len(q) == l**2:
            com = True



    if com:
        k = int(len(q)**(1/2))
        first = heapq.heappop(q)
        x = first[0]
        y = first[1]
        heapq.heappush(q, first)

        for m in range(k):
            for n in range(k):
                next = heapq.heappop(q)
                if x+m == next[0] and y+n == next[1]:
                    result = 'yes'
                    continue
                else:
                    result = 'no'
                    break_t = True
                    break
            if break_t:
                break


    print('#' + str(test + 1), result)