'''
입력
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

#풀이
주어진 정수 list로 
오름차순후 각각 더하여 합

'''
n = int(input())

times = list(map(int, input().split()))

times.sort()
sum = 0

for i in range(n):
    for time in times[0:i+1]:
        sum+=time
        
print(sum)









