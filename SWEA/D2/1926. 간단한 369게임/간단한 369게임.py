test = int(input())
for i in range(1,test+1):
    n = list(str(i))


    if '3' in n or '6' in n or '9' in n:
        count = n.count('3') + n.count('6')+n.count('9')
        for _ in range(count):
            print('-', end='')
        print(' ', end='')

    else:
        print(i, end = ' ')
