




# # class GridWorldProblem:
# #     def __init__(self, grid):
# #         self.grid = grid
# #         self.graph = Graph()
# #         self._build_graph()

# #     def _build_graph(self):
# #         rows = len(self.grid)
# #         cols = len(self.grid[0])
        
# #         for row in range(rows):
# #             for col in range(cols):
# #                 state = (row, col)

# #                 # Add node for current state
# #                 self.graph.add_node(state)

# #                 # Add edges for all possible movements (up, down, left, right)
# #                 if row - 1 >= 0:  # Up
# #                     self.graph.add_edge(state, "up", 1, (row - 1, col))
# #                 if row + 1 < rows:  # Down
# #                     self.graph.add_edge(state, "down", 1, (row + 1, col))
# #                 if col - 1 >= 0:  # Left
# #                     self.graph.add_edge(state, "left", 1, (row, col - 1))
# #                 if col + 1 < cols:  # Right
# #                     self.graph.add_edge(state, "right", 1, (row, col + 1))

# #     def start_state(self):
# #         return (0, 0)  # Example starting state at the top-left corner of the grid

# #     def is_end(self, state):
# #         # Return True if the current state is the bottom-right corner of the grid
# #         return state == (len(self.grid) - 1, len(self.grid[0]) - 1)

# #     def successors(self, state):
# #         # Return the list of successors (neighboring states) with their actions and costs
# #         node = self.graph.get_node(state)
# #         if node is not None:
# #             return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]
# #         return []




# # class MissionariesCannibalsProblem:
# #     def __init__(self, initial_state, goal_state):
# #         self.initial_state = initial_state
# #         self.goal_state = goal_state

# #     def start_state(self):
# #         return self.initial_state

# #     def is_end(self, state):
# #         return state == self.goal_state

# #     def is_valid_state(self, missionaries, cannibals):
# #         """Checks if the state is valid (no more cannibals than missionaries on either bank)."""
# #         if missionaries < 0 or missionaries > 3 or cannibals < 0 or cannibals > 3:
# #             return False
# #         if missionaries > 0 and missionaries < cannibals:
# #             return False  # Left bank: cannibals outnumber missionaries
# #         if missionaries < 3 and (3 - missionaries) < (3 - cannibals):
# #             return False  # Right bank: cannibals outnumber missionaries
# #         return True

# # Robot Problem
# class RobotProblem:
#     def __init__(self, initial_state, goal_state):
#         self.initial_state = initial_state
#         self.goal_state = goal_state
#         self.graph = Graph()
#         self._build_graph()

#     def start_state(self):
#         return self.initial_state

#     def is_end(self, state):
#         return state == self.goal_state

#     def successors(self, state):
#         node = self.graph.get_node(state)
#         if node is not None:
#             return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]
#         return []

#     def _build_graph(self):
#         rows = self.goal_state[0] + 1
#         cols = self.goal_state[1] + 1
#         for i in range(rows):
#             for j in range(cols):
#                 state = (i, j)
#                 self.graph.add_node(state)
#                 if i > 0:
#                     self.graph.add_edge(state, 'up', 1, (i - 1, j))
#                 if i < rows - 1:
#                     self.graph.add_edge(state, 'down', 1, (i + 1, j))
#                 if j > 0:
#                     self.graph.add_edge(state, 'left', 1, (i, j - 1))
#                 if j < cols - 1:
#                     self.graph.add_edge(state, 'right', 1, (i, j + 1))



# #     def successors(self, state):
# #         """Generates valid successor states from the given state."""
# #         successors = []
# #         M_left, C_left, boat_pos = state

# #         moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]  # Possible moves (M, C)

# #         for M_move, C_move in moves:
# #             if boat_pos == 0:  # Boat on the left bank
# #                 new_state = (M_left - M_move, C_left - C_move, 1)  # Move to the right bank
# #             else:  # Boat on the right bank
# #                 new_state = (M_left + M_move, C_left + C_move, 0)  # Move to the left bank

# #             M_new, C_new, _ = new_state
# #             if self.is_valid_state(M_new, C_new):
# #                 # Each move has a cost of 1 (you can adjust the cost as needed)
# #                 successors.append((None, new_state, 1))

# #         return successors

