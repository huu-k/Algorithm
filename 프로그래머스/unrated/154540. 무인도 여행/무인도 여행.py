import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    x_n = len(maps)
    y_n = len(maps[0])
    
    visited = [[False for _ in range(y_n)] for _ in range(x_n)]
    
    
    
    def dfs(x,y):
        
        if x<0 or x>=x_n or y<0 or y>=y_n:
            return False
        
        if maps[x][y] != 'X' and not visited[x][y]:
            count.append(int(maps[x][y]))
            visited[x][y] = True
            
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            
            return True
        return False
    
    for x in range(x_n):
        for y in range(y_n):
            count = []
            if dfs(x,y) == True:
                answer.append(sum(count))
    
    if answer:
        return sorted(answer)
    else:
        return [-1]
    
    
