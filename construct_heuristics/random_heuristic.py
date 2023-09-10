from tsp import TSP 
import random 

def random_heuristic(problem:TSP,rng=random):
    """Random heuristic for TSP problem
    param:
    (TSP) problem: TSP problem model
    ([Optional] random): Random number generator engine 
    return:
    (List[int]) list of the order of nodes 
    """
    nodes = problem.nodes()
    nodes.shuffle(rng)
    return nodes
    
