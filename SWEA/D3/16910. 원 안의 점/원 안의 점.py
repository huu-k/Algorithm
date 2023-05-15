test_case = int(input())

for test in range(test_case):

    n = int(input())
    sum = 0  # (0,0) 포함

    for x in range(0,  n + 1):
        for y in range(0, n + 1):
            if ((x ** 2) + (y**2)) <= n**2:
                if x==0 and y==0:
                    sum+=1
                elif x==0 and y !=0 or y==0 and x !=0:
                    sum+=2

                else:
                    sum+=4

    print('#' + str(test + 1), sum)
