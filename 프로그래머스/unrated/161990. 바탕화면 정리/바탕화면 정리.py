def solution(wallpaper):
    
    start_x, start_y, end_x, end_y = len(wallpaper),len(wallpaper[0]),0,0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] =='#':
                start_x = min(start_x, i)
                start_y = min(start_y, j)
                end_x = max(end_x, i+1)
                end_y = max(end_y, j+1)
            
            
            
            
    
    
    answer = [start_x, start_y, end_x, end_y]
    return answer