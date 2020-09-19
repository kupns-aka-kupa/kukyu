def longestSlideDown(pyramid):
    pass


def slide_down(graph, visited):
    for i in graph:
        print(i)
        if isinstance(graph[i], dict):
            slide_down(graph[i], visited)
        else:
            visited[i] = graph[i]


def list_to_graph(l):
    if isinstance(l, list):
        return {i: list_to_graph(l[i]) for i in range(len(l))}
    else:
        return l
