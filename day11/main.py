from collections import deque


def count_paths(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        adjacency = dict()
        indegrees = dict()
        for line in lines:
            sequence = line.strip().split(' ')
            adjacency[sequence[0][:-1]] = sequence[1:]
            for node in sequence[1:]:
                if node in indegrees:
                    indegrees[node] += 1
                else:
                    indegrees[node] = 1

    no_incoming = deque()
    topological_ordering = []
    for node in adjacency:
        if node not in indegrees:
            no_incoming.append(node)
    while no_incoming:
        node = no_incoming.popleft()
        topological_ordering.append(node)
        if node in adjacency:
            for neighbor in adjacency[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    no_incoming.append(neighbor)

    numpaths = dict()
    print(topological_ordering)
    for node in topological_ordering:
        numpaths[node] = 0
    numpaths["you"] = 1
    for node in topological_ordering:
        if node in adjacency:
            for neighbor in adjacency[node]:
                numpaths[neighbor] += numpaths[node]
    print(numpaths["out"])


def count_paths_through(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        adjacency = dict()
        indegrees = dict()
        for line in lines:
            sequence = line.strip().split(' ')
            adjacency[sequence[0][:-1]] = sequence[1:]
            for node in sequence[1:]:
                if node in indegrees:
                    indegrees[node] += 1
                else:
                    indegrees[node] = 1

    no_incoming = deque()
    topological_ordering = []
    for node in adjacency:
        if node not in indegrees:
            no_incoming.append(node)
    while no_incoming:
        node = no_incoming.popleft()
        topological_ordering.append(node)
        if node in adjacency:
            for neighbor in adjacency[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    no_incoming.append(neighbor)

    numpaths = dict()
    for node in topological_ordering:
        numpaths[node] = 0
    numpaths["svr"] = 1
    for node in topological_ordering:
        if node in adjacency:
            for neighbor in adjacency[node]:
                numpaths[neighbor] += numpaths[node]

    fft = numpaths["fft"]

    for node in topological_ordering:
        numpaths[node] = 0
    numpaths["fft"] = 1
    for node in topological_ordering:
        if node in adjacency:
            for neighbor in adjacency[node]:
                numpaths[neighbor] += numpaths[node]

    dac = numpaths["dac"]

    for node in topological_ordering:
        numpaths[node] = 0
    numpaths["dac"] = 1
    for node in topological_ordering:
        if node in adjacency:
            for neighbor in adjacency[node]:
                numpaths[neighbor] += numpaths[node]

    out = numpaths["out"]

    print(fft * dac * out)


if __name__ == '__main__':
    count_paths("input.txt")
    count_paths_through("input.txt")
