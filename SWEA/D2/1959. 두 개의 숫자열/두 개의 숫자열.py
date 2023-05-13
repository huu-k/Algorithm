test_case = int(input())

def compare (a, b): #len(A)<len(B)
    j = len(b) - len(a)
    result = 0
   
    for k in range(j+1):
        sum=0
        for l in range(len(a)):
            sum += a[l]*b[k+l]
         
        result = max(result, sum)
            
    return result

for i in range(test_case):
    len_a , len_b = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    print('#'+str(i+1), end = ' ')
    if len_a < len_b:
        print(compare(a,b))
    else:
        print(compare(b,a))



