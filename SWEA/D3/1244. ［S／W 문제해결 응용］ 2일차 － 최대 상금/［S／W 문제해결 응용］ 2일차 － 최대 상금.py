T = int(input())
for tc in range(1, T+1):
    n, c = input().split()
    N = len(n)
    num = set([n])  # 중복제거
    com = set()
    c = int(c)

    for _ in range(c): # 횟수만큼 반복
        while num:
            a = list(num.pop())
            for i in range(N):  # powerset 방식
                for j in range(i+1, N):
                    a[i], a[j] = a[j], a[i]
                    com.add(''.join(a))
                    a[i], a[j] = a[j], a[i]
        num, com = com, num  # k만큼 교체 해주면서 모든 경우의 수를 더함

    print('#{} {}'.format(tc, max(num)))