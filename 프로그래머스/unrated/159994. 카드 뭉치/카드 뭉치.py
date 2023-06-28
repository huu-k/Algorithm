from collections import deque


def solution(cards1, cards2, goal):
    card1 = deque(list(cards1))
    card2 = deque(list(cards2))
    answer = 'Yes'
    
    for x in goal:
        if x in card1:
            if x == card1.popleft():
                continue
            else:
                answer = 'No'
                break
        elif x in card2:
            if x == card2.popleft():
                continue
            else:
                answer = 'No'
                break
        else:
            answer = 'No'
            break     
                
        
        
    
    return answer