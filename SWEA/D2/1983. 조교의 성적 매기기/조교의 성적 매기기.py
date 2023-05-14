import heapq

grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

test_case = int(input())

for i in range(test_case):
    n, k = map(int, input().split())
    score = []
    s_grade = [''] * n
    #데이터 입력
    for j in range(n):
    	#중간35, 기말45, 과제20
    	m, f, r = map(int, input().split())
    	heapq.heappush(score, ((m * 0.35 + f * 0.45 + r * 0.2), j))

    for m in range(10):
        for _ in range(n // 10):
            index1 = heapq.heappop(score)
            s_grade[index1[1]] = grade[m]
    print('#' + str(i + 1), end=' ')
    print(s_grade[k - 1])



