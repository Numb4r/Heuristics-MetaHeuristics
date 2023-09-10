import tsplib95 
from typing import List
from pydantic import BaseModel

class TSP(BaseModel):
    """Class representing a TSP model"""
    def __init__(self,filename:str):
        """
        Constructor for TSP model
        parms:
        (string) filename : path to the TSP problem file"""
        self.__data = tsplib95.load(filename)
    def size(self):
        """Return the size of the model dimesion
        return: (int)size of the model"""
        return self.__data.dimension
    def nodes(self):
        """Return a list of nodes of the model
        return : [list] list of nodes of the model"""
        return [i for i in self.__data.get_nodes()]
    def cost(self,i:int,j:int):
        """Return the cost of two nodes of the model
        params:
        (int) i : index node of the model
        (int) j : index node of the model
        return:(float) cost of the edge"""
        return self.__data.get_weight(i,j)
    def evaluate(self,solution:List):
        """Evaluate the model
        param:
        (list) solution: A solution for the problem TSP\
        return:
        (int) Cost of the solution
        """
        cost = 0
        for i,_ in enumerate(solution):
            cost += self.cost(solution[i],solution[(i+1)%self.size()])
        return cost
    def is_valid(self,solution:List):
        """Validate the model
        param:
        (list) solution: A solution for the problem TSP
        return:
        (bool) Return true if the solution is valid
        """
        return len(solution) == self.size() and set(solution) == set(self.nodes)