import copy
from itertools import combinations
for test in range(int(input())):

    arr = list(input())

    result = []#각 결과 저장

    result.append(int(''.join(arr)))

    for i, j in combinations(range(len(arr)), 2):
        old = copy.deepcopy(arr)

        old[i], old[j] = old[j], old[i]

        if old[0] != '0' :
            result.append(int(''.join(old)))
        else:
            continue

    print('#'+str(test+1), min(result), max(result))