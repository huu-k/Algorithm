import heapq
import sys
input = sys.stdin.readline
q = []#우선순위 큐
n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q, x)
    else:
        if len(q)==0:
            print('0')
        else:
            print(heapq.heappop(q))

