import math

def get_distance(x1, x2, y1, y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))


def init_cost(start_node, M):
    costs = {}
    costs[start_node] = 0
    for node in range(len(M.roads)):
        if node != start_node:
            costs[node] = float("inf")
    return costs

def getLowestCost(start_node, costs, parents, M):
    for neighbor in M.roads[start_node]:
        x1, y1 = M.intersections[start_node]
        x2, y2 = M.intersections[neighbor]
        distance = get_distance(x1, x2, y1, y2)
        
        new_cost = costs[start_node] + distance
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = start_node
    return costs

def searchAlgo(start_node, M):
    costs = init_cost(start_node, M)
    parents = {}
    parents[start_node] = None
    visited = []
    
    while start_node is not None:
        min_node = None
        min_cost = None
        visited.append(start_node)
        costs = getLowestCost(start_node, costs, parents, M)
        for node, cost in costs.items():
            if node not in visited:
                if min_node is None:
                    min_node =  node
                    min_cost = cost
                
                if cost < min_cost:
                    min_cost = cost
                    min_node = node
        
        start_node = min_node
    return parents, costs


def findPath(node, pathList, parents):
    pathList.insert(0, node)
    if parents[node] == None:
        return pathList
    
    return findPath(parents[node], pathList, parents)


def shortest_path(M, start, goal):
    print("shortestPath called")
    parents, costs = searchAlgo(start, M)
    pathList = findPath(goal, [], parents)
    return pathList
