import tsplib95 
import os
from typing import List
from pydantic import BaseModel
import networkx as nx
import matplotlib.pyplot as plt
class TSP:
    """
    Class representing a Traveling Salesman Problem (TSP) model.

    This class provides methods to work with TSP instances, including loading data from a file,
    retrieving information about the problem, evaluating solutions, and plotting solutions.

    Args:
        filename (str): Path to the TSP problem file.

    Attributes:
        __data (tsplib95.models.StandardProblem): Internal representation of the TSP data.

    Example:
        tsp = TSP("instance.tsp")
    """
    
    def __init__(self, filename: str):
        """
        Constructor for TSP model.

        Args:
            filename (str): Path to the TSP problem file.
        """
        self.__data = tsplib95.load(filename)

    def size(self):
        """
        Return the size (dimension) of the TSP model.

        Returns:
            int: Size (dimension) of the TSP model.

        Example:
            dimension = tsp.size()
        """
        return self.__data.dimension

    def nodes(self):
        """
        Return a list of nodes in the TSP model.

        Returns:
            list: List of nodes in the TSP model.

        Example:
            node_list = tsp.nodes()
        """
        return list(self.__data.get_nodes())

    def cost(self, i: int, j: int):
        """
        Return the cost of the edge between two nodes in the TSP model.

        Args:
            i (int): Index of the first node.
            j (int): Index of the second node.

        Returns:
            float: Cost of the edge between the two nodes.

        Example:
            edge_cost = tsp.cost(1, 2)
        """
        return self.__data.get_weight(i, j)

    def evaluate(self, solution: List):
        """
        Evaluate the cost of a solution for the TSP model.

        Args:
            solution (list): A solution for the TSP problem as a list of node indices.

        Returns:
            int: Cost of the solution.

        Example:
            solution_cost = tsp.evaluate([1, 2, 3, 4])
        """
        cost = 0
        for i, _ in enumerate(solution):
            cost += self.cost(solution[i], solution[(i + 1) % self.size()])
        return cost

    def is_valid(self, solution: List):
        """
        Validate a solution for the TSP model.

        Args:
            solution (list): A solution for the TSP problem as a list of node indices.

        Returns:
            bool: True if the solution is valid; False otherwise.

        Example:
            valid = tsp.is_valid([1, 2, 3, 4])
        """
        return len(solution) == self.size() and set(solution) == set(self.nodes())

    def plot(self, solution: List):
        """
        Plot the TSP model with the given solution.

        Args:
            solution (list): A solution for the TSP problem as a list of node indices.

        Example:
            tsp.plot([1, 2, 3, 4])
        """
        G = nx.DiGraph()
        fixed_pos = {}
        for node in self.__data.get_nodes():
            G.add_node(node)
            fixed_pos[node] = self.__data.node_coords[node]
        for i, node in enumerate(solution[:-1]):
            G.add_edge(node, solution[i + 1])
        G.add_edge(solution[-1], solution[0])
        nx.set_node_attributes(G, fixed_pos, "pos")
        node_positions = nx.get_node_attributes(G, "pos")
        pos = node_positions
        options = {
            'with_labels': True,
            'node_color': 'skyblue',
            'node_size': 500,
        }
        nx.draw(G, pos, **options)
        folder = "out"
        if not os.path.exists(folder):
            os.makedirs(folder)
        plt.savefig('out/grafo.png')
