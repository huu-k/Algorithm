n, k = map(int, input().split())

line =[]
for i in range(n):
    line.append(int(input()))

#이진탐색하여 갯수 확인
start = 1
end = max(line)
result = 0
while start<=end:
    mid = (start+end)//2 #자르려고 하는 길이

    #동일 길이 랜선의 개수
    count =0
    for i in line:
        count+= i//mid



    #작거나 클 경우
    if count >= k:
        start = mid+1
    else:
        end = mid-1
        

print(end)
