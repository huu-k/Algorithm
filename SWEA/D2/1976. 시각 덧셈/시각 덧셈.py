test_case = int(input())
for i in range(test_case):
    m1, s1, m2, s2 = map(int, input().split())
    s = (s1+s2)
    m = (m1+m2)
    if s >= 60:
        s-=60
        m+=1
    
    if m >12:
        m-=12
    
 
    print('#'+str(i+1), m, s)