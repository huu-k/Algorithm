#일수로 구하기
def daytime(today):
    ty, tm, td = map(int,today.split('.'))
    #한달을 28일로 계산
    return (ty*12*30) + (tm*30) +td

def solution(today, terms, privacies):
    
    today = daytime(today)
    
    terms = {x.split(' ')[0]:int(x.split(' ')[1]) for x in terms}
    answer = []
    
    for x_index, x in enumerate(privacies):
        cal , term = x.split(' ')
        
        x_cal = daytime(cal) + (terms[term]*30)
        
        if x_cal <= today:
            answer.append(x_index+1)
        
    return answer