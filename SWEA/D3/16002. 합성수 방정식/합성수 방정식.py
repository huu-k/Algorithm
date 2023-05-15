test_case = int(input())
MAX = 10**9

def divisor(x):
    for j in range(2, int(x**(1/2))+1):
        if x%j==0:
            return True
    return False    	
          
                   


for test in range(test_case):
    n = int(input())
    
    print('#'+str(test+1), end=' ')
    
    for i in range(MAX-n,0,-1):
        a = i 
        b = i-n
        
        if divisor(a) and divisor(b):
            print(a, b)
            break
            
        
    
    
    
    
    
    
    
 