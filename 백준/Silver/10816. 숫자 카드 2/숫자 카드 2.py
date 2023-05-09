#내풀이 bisect
from bisect import bisect_left, bisect_right

#갯수구하기
def bisect_count(arr,x):
    right_value = bisect_right(arr,x)
    left_value = bisect_left(arr, x)
    return right_value - left_value
n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
find = list(map(int, input().split()))
count=[0]*m

for i in range(m):
    count[i] = bisect_count(card, find[i])

for x in count:
    print(x, end = ' ')