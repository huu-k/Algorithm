from collections import deque

for test in range(10):
    t = input()
    q = deque(list(map(int, input().split())))
    break_t = False
    while q:
        for i in range(1, 6):
            q_pop = q.popleft()
            q_pop -= i
            if q_pop <= 0:
                q.append(0)
                print('#' + str(test+1), *q, sep=' ')
                break_t = True
                break

            else:
                q.append(q_pop)
        if break_t:
            break