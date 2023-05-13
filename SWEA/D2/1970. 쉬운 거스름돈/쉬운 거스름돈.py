'''
50,000 원 : 0개
10,000 원 : 3개
5,000 원 : 0개
1,000 원 : 2개
500 원 : 1개
100 원 : 3개
50 원 : 1개
10 원 : 0개
'''
test_case = int(input())
money = [50000,10000,5000,1000,500,100,50,10]

for i in range(test_case):
    count=[0]*8
    n = int(input())
    
    print('#'+str(i+1))
    for j in range(len(money)):

        if n//money[j]!=0:
            count[j] = n//money[j]
            n = n%money[j]
            
    for k in range(len(count)):
        print(count[k], end=' ')
    print()
    

        
        