def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    new_score = [score[i:i+m] for i in range(0,len(score), m)]
    
    for i in range(len(score)//m):
        answer += (min(new_score[i])*m*1)
    
   
    return answer