def solution(name, yearning, photo):
    answer = []
    for p in photo:
        sum = 0
        for x in p:
            if x in name:
                sum+=yearning[name.index(x)]
            
        answer.append(sum)
            
    
    
    return answer