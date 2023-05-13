

test_case = int(input())

def n_count(count, n):
    arr = list(str(n))
    for i in range(len(arr)):
        count[int(arr[i])]+=1

for i in range(test_case):
    count = [0]*10
    n = int(input())
    k = 0
    while 0 in count:
        k+=1
        new_n = n*k
        n_count(count,new_n)


    print('#'+str(i+1), new_n)
    count.clear()


