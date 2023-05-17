for test in range(int(input())):

    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 우, 하, 좌 , 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, 0
    dist = 0
    for i in range(1, (N * N) + 1):
        arr[x][y] = i
        x += dx[dist]
        y += dy[dist]

        # 범위가 넘어가거나 이미 수가 채워진 경우
        if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] != 0:
            x -= dx[dist]
            y -= dy[dist]
            dist = (dist + 1) % 4

            # 긔
            x += dx[dist]
            y += dy[dist]

    print('#' + str(test + 1))

    for x in arr:
        print(*x)

