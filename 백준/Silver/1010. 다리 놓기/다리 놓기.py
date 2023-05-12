test_case = int(input())

#팩
def fac (n):
    f = 1
    for i in range(1,n+1):
        f *=i
    return f



for _ in range(test_case):
    n, m = map(int,input().split())

    mcn = fac(m) // (fac(n)*fac(m-n))

    print(mcn)