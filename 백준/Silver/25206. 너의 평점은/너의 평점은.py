sum_score =0.0

sum = 0.0

degree_dic = {'A+':4.5,'A0' : 4.0,'B+' : 3.5,'B0' : 3.0,'C+' : 2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

for _ in range(20):
    student = list(input().split())
    if(student[2]=='P'):
        continue
    else:
        sum += float(student[1])*degree_dic[student[2]]
        sum_score +=float(student[1])
            


#전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.

print(sum/sum_score)