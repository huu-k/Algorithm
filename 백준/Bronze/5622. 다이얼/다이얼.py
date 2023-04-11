aList = [ 'ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

number = list(input())

clockSum =0

for i in number:
    for j in aList:
        if(i in j):
            clockSum += aList.index(j) +3 #abc = 3 즉, index +3

print(clockSum)

