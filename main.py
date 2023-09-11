import argparse
import random
from tsp import TSP 
from construct_heuristics.random_heuristic import random_heuristic
from construct_heuristics.fih import farthest_insertion_heuristic
from construct_heuristics.nih import nearest_insertion_heuristic
from construct_heuristics.nnh import nearest_neighbor_heuristic
def main()->None:
    """
    Main function for running a Traveling Salesman Problem (TSP) solver.

    This program takes a file path to a TSP instance, an algorithm choice, and an optional
    random seed to solve the TSP and display results.

    Args:
        None

    Returns:
        None

    Example:
        To run the program:
        $ python program_name.py instance.tsp -a 1 -s 12345
    Arguments:
        filepath (str): The file path to the TSP instance file.
            This argument is required.
        
        -a, --algorithm (int): The algorithm choice for solving the TSP.
            Choose from the following options:
            1: Random Heuristic
            2: Nearest Insertion Heuristic
            3: Nearest Neighbor Heuristic
            4: Farthest Insertion Heuristic
            This argument is required.
        
        -s, --seed (int, optional): The random seed to initialize randomness (default: 0).
            Use this argument to reproduce results when using random-based algorithms.
    """
    parser = argparse.ArgumentParser(
        prog='program_name.py',
        description='A program to solve the Traveling Salesman Problem (TSP).',
        epilog='Example usage: python program_name.py instance.tsp -a 1 -s 12345'
    )
    
    parser.add_argument('filepath',
                        help='The file path to the TSP instance file (e.g., "instance.tsp"). This argument is required.')
    
    parser.add_argument('-a', '--algorithm', type=int, required=True,
                        choices=[1, 2, 3, 4],
                        help='The algorithm choice for solving the TSP. Choose from the following options:\n'
                             '1: Random Heuristic\n'
                             '2: Nearest Insertion Heuristic\n'
                             '3: Nearest Neighbor Heuristic\n'
                             '4: Farthest Insertion Heuristic\n'
                             'This argument is required.')
    
    parser.add_argument('-s', '--seed', type=int, required=False, default=0,
                        help='The random seed to initialize randomness (default: 0). Use this argument to reproduce '
                             'results when using random-based algorithms.')
    
    args = parser.parse_args()
    
    tsp = TSP(args.filepath)
    random.seed(args.seed)
    start_node = tsp.nodes()[0]
    match args.algorithm:
        case 1:
            problem = random_heuristic(tsp,random)
        case 2:
            problem = nearest_insertion_heuristic(tsp,start_node)
        case 3:
            problem = nearest_neighbor_heuristic(tsp,start_node)
        case 4:
            problem = farthest_insertion_heuristic(tsp,start_node)
        case _:
            print("No algorithm specified")
            problem =[]
    if len(problem) != 0:
        print(f"O problema e valido:{tsp.is_valid(problem)}")
        print(f"Custo do problema: {tsp.evaluate(problem)}")
        tsp.plot(problem)

if __name__ == "__main__":
    main()