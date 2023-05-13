'''
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.

출력
첫째 줄에 최소 비교 횟수를 출력한다.'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    heapq.heappush(q, x)
    
sum = 0

for i in range(n-1): #두개씩 꺼내야하기 때문
    now = heapq.heappop(q)
    next = heapq.heappop(q)
    
    sum+= now+next
    
    heapq.heappush(q, now+next)
print(sum)

