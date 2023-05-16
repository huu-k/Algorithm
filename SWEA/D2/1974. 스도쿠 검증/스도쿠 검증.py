def width(arr):
    for i in range(9):
        count = [0] * 9
        for j in range(9):
            count[arr[i][j] - 1] += 1
        if 0 in count:
            return 0
    return 1

def height(arr):
    for i in range(9):
        count = [0] * 9
        for j in range(9):
            count[arr[j][i] - 1] += 1
        if 0 in count:
            return 0
    return 1

def three(arr):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = [0] * 9
            for m in range(3):
                for n in range(3):
                    count[arr[i + m][j + n] - 1] += 1
            if 0 in count:
                return 0
    return 1

for test in range(int(input())):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))

    # 가로
    w = width(arr)
    h = height(arr)
    t = three(arr)
    #print(w,h,t)

    result = w and h and t

    print('#' + str(test + 1), result)