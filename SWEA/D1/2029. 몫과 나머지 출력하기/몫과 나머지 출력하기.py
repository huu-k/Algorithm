test_case = int(input())

for i in range(test_case):
    a,b = map(int, input().split())
    
    print('#'+str(i+1), a//b, a%b)