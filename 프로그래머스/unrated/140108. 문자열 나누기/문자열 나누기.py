from collections import deque

def solution(s):
    answer = 0
    correct = 0
    incorrect = 0
    s_q = deque([x for x in s])
    first = s[0]
    
    while s_q:
        ss = s_q.popleft()

        if ss == first:
            correct+=1
        else:
            incorrect+=1
            
        if incorrect== correct:
            
            answer += 1 
            incorrect, correct = 0,0
            if s_q:
                first = s_q[0]
        elif not s_q:
            answer +=1 
            break
            
            
        
        
        
    
    
    return answer