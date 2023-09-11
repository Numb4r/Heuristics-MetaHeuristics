from tsp import TSP 
import random 

def random_heuristic(problem: TSP, rng=random):
    """
    Random heuristic for the Traveling Salesman Problem (TSP).

    This heuristic generates a random order of nodes as a possible solution to the TSP problem.

    Args:
        problem (TSP): The TSP problem model.
        rng (Optional[random]): Random number generator engine (default: random module).

    Returns:
        List[int]: A list representing the order of nodes in the generated solution.

    Example:
        solution = random_heuristic(tsp_instance)
    """
    nodes = problem.nodes()
    rng.shuffle(nodes)
    return nodes
