def solution(s):
    answer = []
    for i in range(len(s)):
        index = 0
        if s[i] in s[:i]:
            for j in range(i-1, -1, -1):
                index+=1
                if s[i]==s[j]:
                    answer.append(index)
                    break
        else:
            answer.append(-1)
        
        
        
    return answer