#딕셔너리로 날짜 저장 후 해당하는 날짜의 달에서 뺀 값으 나머지 날과 더하기

test_case = int(input())

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(test_case):
    m1, d1, m2, d2 = map(int,input().split())
    
    print('#'+str(i+1), end=' ')
    
    if m1 == m2:
        print(d2-d1+1)
    
    else:
        sum = 1 + day[m1]-d1 +d2
        for m in range(m1+1, m2):
            sum+=day[m]
            
        print(sum)
        