'''
N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.
'''

test_case= int(input())

for i in range(test_case):
    count= [0]*5
    n = int(input())
    while n != 1:
        if (n%2 == 0):
        	count[0]+=1
        	n = n//2
        if (n%3 == 0):
        	count[1]+=1
        	n = n//3
        if (n%5 == 0):
        	count[2]+=1
        	n = n//5
        if (n%7 == 0):
        	count[3]+=1
        	n = n//7        
        if (n%11 == 0):
        	count[4]+=1
        	n = n//11   
            
	
    print('#'+str(i+1), end=' ')
    for x in count:
    	print(x, end=' ')
        
    print()
    count.clear()