abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for test in range(int(input())):
    n = list(input())
    count=0
    
    for i in range(len(n)):
        if abc[i] == n[i]:
            count+=1
        else:
            break



    print('#' + str(test + 1), count)