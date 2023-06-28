def solution(park, routes):
    graph = []
    route = []
    n = len(park)
    m = len(park[0])
    op_x = {'N': 0, 'S': 0, 'W': -1, 'E': 1}
    op_y = {'N': -1, 'S': 1, 'W': 0, 'E': 0}

    # graph
    for x in park:
        graph.append(list(x))

    # route
    for x in routes:
        route.append(x.split())

    # start point
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if 'S' == graph[i][j]:
                start = [i, j]

    for route in routes:
        op = route[0]
        op_n = int(route[2])

        or_start = start.copy()

        for _ in range(op_n):
            n_start = start
            n_start[0] += op_y[op]
            n_start[1] +=  op_x[op]

            if (0 <= start[0] < n) and (0 <= start[1] < m) and (park[n_start[0]][n_start[1]] != 'X'):
                start = n_start.copy()
            else:
                start = or_start.copy()
                break

    return start
