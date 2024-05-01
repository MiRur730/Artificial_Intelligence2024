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

    def move_first_empty_tile(self, direction):
        new_empty_indices = list(self.empty_tiles)
        if direction == "up":
            if new_empty_indices[0] - 3 >= 0:
                new_empty_indices[0] -= 3
            else:
                return None
        elif direction == "down":
            if new_empty_indices[0] + 3 < len(self.current_state):
                new_empty_indices[0] += 3
            else:
                return None
        return new_empty_indices

    def move_second_empty_tile(self, direction):
        new_empty_indices = list(self.empty_tiles)
        if direction == "up":
            if new_empty_indices[1] - 3 >= 0:
                new_empty_indices[1] -= 3
            else:
                return None
        elif direction == "down":
            if new_empty_indices[1] + 3 < len(self.current_state):
                new_empty_indices[1] += 3
            else:
                return None
        return new_empty_indices

    def move(self, direction):
        temp_state = self.current_state[:]
        new_empty_indices = self.move_first_empty_tile(direction)
        if new_empty_indices is None:
            new_empty_indices = self.move_second_empty_tile(direction)
        if new_empty_indices is None:
            return None

        temp_state = self.move_empty_tiles(new_empty_indices)

        return Puzzle(temp_state, self.goal_state, self.current_state)

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

    p.steepesthill_climbing()
              
if __name__ == "__main__":
    main()
