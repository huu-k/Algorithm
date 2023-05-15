
test_case = int(input())

for test in range(test_case):
    arr = []
    n, k = map(int, input().split())
    sum = 0

    # 데이터 저장
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n-k+1):
        for j in range(n-k+1):
            n_sum = 0

            for i_k in range(k):
                for j_k in range(k):
                    n_sum += arr[i + i_k][j + j_k]

            sum = max(sum, n_sum)

    print('#' + str(test + 1), end=' ')
    print(sum)