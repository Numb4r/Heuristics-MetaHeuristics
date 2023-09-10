from tsp import TSP
import math 

def farthest_insertion_heuristic(problem:TSP,start_node):
    """Farthest insertion heuristic for TSP problem
    param:
    (TSP) problem: TSP problem model
    ([Optional] random): Random number generator engine 
    return:
    (List[int]) list of the order of nodes 
    """
    solution = [start_node]
    nodes = problem.nodes()
    nodes.remove(start_node)

    while len(nodes) > 0:
        best_node = None
        best_index = None
        best_cost = math.inf
        for node in nodes:
            for s_n in solution:
                cost = problem.cost(node,s_n)
                if cost < best_cost:
                    best_node = node
                    best_cost = cost

        best_index = len(solution)
        best_cost = 0
        if(len(solution)>1):
            for i,_ in enumerate(solution):
                cost = (problem.cost(solution[i-1],best_node)
                        +problem.cost(best_node,solution[i])
                        -problem.cost(solution[i-1],solution[i]))
                if cost > best_cost:
                    best_index = i 
                    best_cost = cost
        solution.insert(best_index, best_node)
        nodes.remove(best_node)