'''
N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.
'''

test_case= int(input())

for j in range(test_case):
    count= [0]*5
    num = [2,3,5,7,11]
    n = int(input())
    while n != 1:
        for i in range(5):
            if n%num[i]==0:
                count[i]+=1
                n//=num[i]
            
	
    print('#'+str(j+1), end=' ')
    for x in count:
    	print(x, end=' ')
        
    print()
    count.clear()