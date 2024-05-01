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

    def dls(self, max_depth):
        stack = [(self.current_state, 0)]  # Include depth information
        
        while stack:
            temp, depth = stack.pop()
            print("Depth:", depth, "State:", temp)
            if temp == self.goal_state:
                print("Goal state has been reached!")
                return True
            
            if depth < max_depth:
                neighbors = self.generate_neighbors(temp)
                for neighbor in neighbors:
                    stack.append((neighbor, depth + 1))
        
        return False

def main():
    my_list = [1, 2, 3, 0, 4, 6, 7, 8, 9]
    goal_list = [1, 2, 3, 4, 0, 6, 7, 8, 9]

    p = Puzzle(my_list, goal_list)

    print("Initial State:")
    p.display_state()

    print("\nDLS with depth limit 3:")
    p.dls(3)


if __name__ == "__main__":
    main()
