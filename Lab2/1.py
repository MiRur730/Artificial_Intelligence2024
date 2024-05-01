from collections import deque

class PuzzleNode:
    def _init_(self, state, parent=None, action=""):
        self.state = state
        self.parent = parent
        self.action = action

    def _eq_(self, other):
        return self.state == other.state

    def _hash_(self):
        return hash(str(self.state))

    def _str_(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state])

    def get_blank_position(self):
        for i, row in enumerate(self.state):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j

    def get_neighbors(self):
        i, j = self.get_blank_position()
        neighbors = []
        moves = [(0, 1, "right"), (0, -1, "left"), (1, 0, "down"), (-1, 0, "up")]
        for dx, dy, action in moves:
            new_i, new_j = i + dx, j + dy
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in self.state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                neighbors.append(PuzzleNode(new_state, parent=self, action=action))
        return neighbors

    def is_goal(self, goal_state):
        return self.state == goal_state

def bfs(start_state, goal_state):
    visited = set()
    queue = deque([PuzzleNode(start_state)])

    while queue:
        current_node = queue.popleft()
        if current_node.is_goal(goal_state):
            return current_node
        visited.add(current_node)
        for neighbor in current_node.get_neighbors():
            if neighbor not in visited:
                queue.append(neighbor)
    return None

def dfs(start_state, goal_state):
    visited = set()
    stack = [PuzzleNode(start_state)]

    while stack:
        current_node = stack.pop()
        if current_node.is_goal(goal_state):
            return current_node
        visited.add(current_node)
        for neighbor in current_node.get_neighbors():
            if neighbor not in visited:
                stack.append(neighbor)
    return None
# Define initial and goal states for test case
test_start_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
test_goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Perform BFS
print("BFS:")
bfs_solution = bfs(test_start_state, test_goal_state)
if bfs_solution:
    print(bfs_solution)
else:
    print("No solution found.")

# Perform DFS
print("\nDFS:")
dfs_solution = dfs(test_start_state, test_goal_state)
if dfs_solution:
    print(dfs_solution)
else:
    print("No solution found.")