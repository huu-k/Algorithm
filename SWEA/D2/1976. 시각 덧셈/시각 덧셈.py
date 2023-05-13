test_case = int(input())
for i in range(test_case):
    m1, s1, m2, s2 = map(int, input().split())
    s = (s1+s2)%60
    m = (m1+m2+((s1+s2)//60))
    if m > 12:
        m-=12
    print('#'+str(i+1), m, s)