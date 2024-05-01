
# for two missing tile problem 
class Puzzle(object):
    
    def __init__(self, initial_state, goal_state):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.empty_tiles = self.get_empty_indices()

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

    def move(self, dir):
        new_empty_indices = list(self.empty_tiles)

        if dir == "up":
            for i in range(len(self.empty_tiles)):
                if self.empty_tiles[i] - 3 >= 0:
                    new_empty_indices[i] = self.empty_tiles[i] - 3
                else:
                    return None
    
        elif dir == "down":
            for i in range(len(self.empty_tiles)):
                if self.empty_tiles[i] + 3 < len(self.current_state):
                    new_empty_indices[i] = self.empty_tiles[i] + 3
                else:
                    return None
        elif dir == "right":
            for i in range(len(self.empty_tiles)):
                if (self.empty_tiles[i] + 1) % 3 != 0:
                    new_empty_indices[i] = self.empty_tiles[i] + 1
                else:
                    return None
        elif dir == "left":
            for i in range(len(self.empty_tiles)):
                if self.empty_tiles[i] % 3 != 0:
                    new_empty_indices[i] = self.empty_tiles[i] - 1
                else:
                    return None
        else:
            return None

        temp = self.move_empty_tiles(new_empty_indices)
        return Puzzle(temp, self.goal_state)

    def goal_checking(self):
        return self.current_state == self.goal_state

    def display_state(self):
        for i in range(3):
            print(self.current_state[i * 3:i * 3 + 3])   

    def misplaced_tiles(self):
        return sum([1 if self.current_state[i] != self.goal_state[i] else 0 for i in range(len(self.current_state))])

    def best_first_search(self):
        priority_queue = [(self.misplaced_tiles(), self)]
        
        while priority_queue:
            priority_queue.sort()  # Sort based on evaluation function
            _, puzzle = priority_queue.pop(0)  # Pop the state with the lowest evaluation
            if puzzle.goal_checking():
                print("Goal state reached")
                break
            
            for direction in ["up", "down", "right", "left"]:
                new_state = puzzle.move(direction)
                if new_state is not None:
                    priority_queue.append((new_state.misplaced_tiles(), new_state))

            self.current_state = puzzle.current_state
            self.empty_tiles = puzzle.empty_tiles
            self.display_state()


def main():
    my_list = [0,3,6,1,2,0,4,5,7]  
    goal_list = [1,2,3,4,5,6,7,0,0]

    p = Puzzle(my_list, goal_list)

    print("Initial State")
    p.display_state()

    p.best_first_search()
              
if __name__ == "__main__":
    main()
