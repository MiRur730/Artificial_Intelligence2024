class Puzzle(object):
    
    def __init__(self, initial_state, goal_state):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.empty_tile = self.get_empty_index()
    
    def move_empty_tile(self, new_empty_index):
        temp_state = self.current_state[:]
        temp_state[self.empty_tile] = temp_state[new_empty_index]
        temp_state[new_empty_index] = 0
        return temp_state
    
    def down(self):
        if self.empty_tile + 3 < 9:
            new_empty_index = self.empty_tile + 3
            return self.move_empty_tile(new_empty_index)
        else:
            return None
    
    def up(self):
        if self.empty_tile - 3 >= 0:
            new_empty_index = self.empty_tile - 3
            return self.move_empty_tile(new_empty_index)
        else:
            return None
    
    def right(self):
        if (self.empty_tile + 1) % 3 != 0:
            new_empty_index = self.empty_tile + 1 
            return self.move_empty_tile(new_empty_index)
        else:
            return None
    
    def left(self):
        if self.empty_tile % 3 != 0:
            new_empty_index = self.empty_tile - 1
            return self.move_empty_tile(new_empty_index)
        else:
            return None  
    
    def get_empty_index(self):
        for i in range(9):
            if self.current_state[i] == 0:
                return i   
    
    def goal_checking(self):
        if self.current_state == self.goal_state:
            print("Goal state has been reached! Stop")

    def display_state(self):
        for i in range(3):
            print(self.current_state[i * 3:i * 3 + 3])   

    def generate_neighbors(self, temp_state):
        self.current_state = temp_state
        neighbors = []

        for move in [self.up(), self.down(), self.left(), self.right()]:
            if move is not None:
                neighbors.append(move)
        
        return neighbors

    def dfs(self, max_depth, open_list, closed_set):
        stack = [(self.current_state, 0)]  # Include depth information
        is_visited = set()
        is_visited.add(tuple(self.current_state))
        
        while stack:
            temp, depth = stack.pop()
            closed_set.add(tuple(temp))  # Add current state to closed set
            print("Depth:", depth, "State:", temp)
            if temp == self.goal_state:
                print("Goal state has been reached!")
                return True
            
            if depth < max_depth:
                neighbors = self.generate_neighbors(temp)
                for neighbor in neighbors:
                    if tuple(neighbor) not in is_visited and tuple(neighbor) not in open_list and tuple(neighbor) not in closed_set:
                        stack.append((neighbor, depth + 1))
                        open_list.add(tuple(neighbor))
                        is_visited.add(tuple(neighbor))
        
        return False

    def iddfs(self):
        depth = 0
        while True:
            print("Depth Limit:", depth)
            open_list = set()
            closed_set = set()
            if self.dfs(depth, open_list, closed_set):
                return True
            else:
                depth += 1
                print("Increasing depth limit to", depth)
        

def main():
    my_list = [1, 2, 3, 0, 4, 6, 7, 8, 9]
    goal_list = [1, 2, 3, 4, 0, 6, 7, 8, 9]

    p = Puzzle(my_list, goal_list)

    print("Initial State:")
    p.display_state()

    print("\nIDDFS:")
    p.iddfs()


if __name__ == "__main__":
    main()
