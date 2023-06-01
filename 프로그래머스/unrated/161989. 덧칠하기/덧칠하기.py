def solution(n, m, section):
    answer = 0
    paint = [False]*(n+1)
    answer=0
    
    for x in section:
        if not paint[x]:
            for i in range(m):
                if x+i<=n:
                    paint[x+i] = True
            answer+=1
        
        
    return answer