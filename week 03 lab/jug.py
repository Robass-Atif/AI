from Graph import Graph
from Searchalgo import BestFirstSearch,DepthFirstSearch,UniformCostSearch

class jugProblem:
    def __init__(self,intial_state,goal_state):
        self.intial_state=intial_state
        self.goal_state=goal_state
        self.graph=Graph()
        self._build_graph()

    def _build_graph():
             
    