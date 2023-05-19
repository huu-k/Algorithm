for test in range(int(input())):
    n, m = map(int,input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = 1

    visited = [False]*(n+1)

    def dfs(graph, v, count):
        global result
        result = max(result, count)
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                
                dfs(graph, i,count+1)
        visited[v] = False

    for j in range(1,n+1):
        dfs(graph,j, 1)

    print(f"#{test+1} {result}")
