class Puzzle(object):
    
    def __init__(self, initial_state, goal_state, parent=None):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.empty_tiles = self.get_empty_indices()
        self.parent = parent

    def get_empty_indices(self):
        indexes = []
        for i in range(len(self.current_state)):
            if self.current_state[i] == 0:
                indexes.append(i)
        return indexes

    def move_empty_tiles(self, new_empty_indices):
        temp_state = self.current_state[:]
        for i in range(len(self.empty_tiles)):
            temp_state[self.empty_tiles[i]] = temp_state[new_empty_indices[i]]
            temp_state[new_empty_indices[i]] = 0
        self.empty_tiles = new_empty_indices
        return temp_state




# this we need for two 
    def move(self, direction):
        #two new index we will get
        new_empty_indices = list(self.empty_tiles)

        # this will chek up condition  for both empty indexes 
        if direction == "up":
            for i in range(len(self.empty_tiles)):
                if self.empty_tiles[i] - 3 >= 0:
                    new_empty_indices[i] = self.empty_tiles[i] - 3
                else:
                    return None
                
        elif direction == "down":
            for i in range(len(self.empty_tiles)):
                if self.empty_tiles[i] + 3 < len(self.current_state):
                    new_empty_indices[i] = self.empty_tiles[i] + 3
                else:
                    return None
        elif direction == "right":
            for i in range(len(self.empty_tiles)):
                if (self.empty_tiles[i] + 1) % 3 != 0:
                    new_empty_indices[i] = self.empty_tiles[i] + 1
                else:
                    return None
        elif direction == "left":
            for i in range(len(self.empty_tiles)):
                if self.empty_tiles[i] % 3 != 0:
                    new_empty_indices[i] = self.empty_tiles[i] - 1
                else:
                    return None
        else:
            return None

       # whatever is possible it will move to that 
        temp = self.move_empty_tiles(new_empty_indices)
        return Puzzle(temp, self.goal_state, self.current_state)

    def goal_checking(self):
        return self.current_state == self.goal_state

    def display_state(self):
        for i in range(3):
            print(self.current_state[i * 3:i * 3 + 3])   

    def calculate_heuristic(self):
        return sum([1 if self.current_state[i] == self.goal_state[i] else 0 for i in range(len(self.current_state))])

    def steepesthill_climbing(self):
        while True:
            parent = self
            if self.current_state == self.goal_state:
                print("Goal state has been reached! Stop")
                break
            
            heuristic = self.calculate_heuristic()
            best_move = None
            
            for direction in ["up", "down", "right", "left"]:
                new_state = parent.move(direction)
                if new_state is not None:
                    h = new_state.calculate_heuristic()
                    if h < heuristic:
                        heuristic = h
                        best_move = new_state

            if best_move is None:
                print("Cannot improve heuristic. Stopping.")
                break

            self.current_state = best_move.current_state 
            self.empty_tiles = best_move.empty_tiles
            self.display_state() 

def main():
    my_list = [0, 0, 3, 1, 2, 0, 4, 5, 6]  
    goal_list = [1, 2, 3, 4, 5, 6, 0, 0, 0]

    p = Puzzle(my_list, goal_list)

    print("Initial State")
    p.display_state()

    p.steepesthill_climbinghill_climbing()
              
if __name__ == "__main__":
    main()
