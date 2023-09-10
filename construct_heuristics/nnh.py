from tsp import TSP 
import math 

def nearest_neighbor_heuristic(problem:TSP, start_node):
    """nearest neighbor heurist for TSP problem
    param:
    (TSP) problem: TSP problem model
    (int) start_node: start point for the heuristic
    return:
    (List[int]) list of the order of nodes 
    """
    solution = [start_node]
    nodes = problem.nodes()
    nodes.remove(start_node)
    while len(nodes)>0:
        last_node = solution[-1]
        best_node = None
        best_cost = math.inf
        for node in nodes:
            cost  = problem.cost(last_node, node)
            if cost < best_cost:
                best_cost = cost
                best_node = node
            solution.append(best_node)
            nodes.remove(best_node)
    return solution