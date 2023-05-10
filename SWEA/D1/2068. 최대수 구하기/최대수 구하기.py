test_case = int(input())

for i in range(test_case):
    arr = list(map(int, input().split()))
    
    print('#'+str(i+1), max(arr))