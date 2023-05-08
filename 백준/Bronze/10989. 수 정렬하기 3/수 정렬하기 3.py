'''
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.'''
import sys

n = int(input())
count = [0]*10001

for i in range(n):
    a = int(sys.stdin.readline())
    count[a]+=1
 
for i in range(len(count)): #리스트에 기록된 정렬 정보 확인, 각각의 인덱스를 확인하면서
	for j in range(count[i]):
		print(i) #띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력