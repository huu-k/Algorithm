n_test = int(input())
count=0

for _ in range(n_test):
    score = list(map(int, input().split()))
     #round(num, 숫자) : 소수 몇째자리까지 출력
    #평균 출력
    avg = (sum(score[1:])/score[0])

    #평균 이상인 학생 수
    for i in range(score[0]):
        if(score[i+1]>avg):
            count+=1

    per_score = (count/score[0])*100
    print('%.3f' %per_score + '%')

    #count 초기화
    count =0
    
