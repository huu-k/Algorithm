for test in range(int(input())):
    
    n = list(input())
    s=0
    
    for i in range(1, len(n)):
        if n[0] != n[i] or n[1] !=n[i+1]:
            s+=1
        else:
            break
    
    
    
    print('#'+str(test+1),s+1 ) #0번 인덱스 값을더해야하기 때문에