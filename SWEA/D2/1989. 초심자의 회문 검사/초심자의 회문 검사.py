test_case = int(input())
for j in range(test_case):
    n = input().strip()
    new_n = ''
    for i in range(len(n) - 1, -1, -1):
        new_n += n[i]

    print('#' + str(j+1), end=' ')
    if n == new_n:
        print('1')
    else:
        print('0')

