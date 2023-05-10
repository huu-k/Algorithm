calen = {1:31, 2:28, 3:31, 4:30, 5: 31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

test_case = int(input())
for i in range(test_case):
    cal = str(input())

    year = cal[0:4]
    month = cal[4:6]
    day =cal[6:]

    if 0<int(month)< 13 and 0< int(day) <= calen[int(month)] :
        print('#'+str(i+1), year +'/'+month +'/' + day)
    else:
        print('#'+str(i+1), -1)
