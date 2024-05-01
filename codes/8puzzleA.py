# A* 8 PUZZLE PROBLEM

class Puzzle(object):
    
    def __init__(self, initial_state, goal_state,parent=None):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.empty_tile = self.get_empty_index()
        self.parent = parent
        self.g = 0  # Cost from initial state to current state
        self.h = self.calculate_heuristic()  # Heuristic cost from current state to goal state

    def get_empty_index(self):
        for i in range(9):
            if self.current_state[i] == 0:
                return i   

    def move_empty_tile(self, new_empty_index):
        temp_state = self.current_state[:]
        temp_state[self.empty_tile] = temp_state[new_empty_index]
        temp_state[new_empty_index] = 0
        self.empty_tile = new_empty_index
        return temp_state

    def down(self):
        self.empty_tile = self.get_empty_index()
        if self.empty_tile + 3 < 9:
            new_empty_index = self.empty_tile + 3
            temp = self.move_empty_tile(new_empty_index)
            return Puzzle(temp, self.goal_state, self.current_state)
        else:
            return None 
       
    def up(self):
        self.empty_tile = self.get_empty_index()
        if self.empty_tile - 3 >= 0:
            new_empty_index = self.empty_tile - 3
            temp = self.move_empty_tile(new_empty_index)
            return Puzzle(temp, self.goal_state, self.current_state)
        else:
            return None

    def right(self):
        self.empty_tile = self.get_empty_index()
        if (self.empty_tile + 1) % 3 != 0:
            new_empty_index = self.empty_tile + 1 
            temp = self.move_empty_tile(new_empty_index)
            return Puzzle(temp, self.goal_state, self.current_state)
        else:
            return None

    def left(self):
        self.empty_tile = self.get_empty_index()
        if self.empty_tile % 3 != 0:
            new_empty_index = self.empty_tile - 1
            temp = self.move_empty_tile(new_empty_index)
            return Puzzle(temp, self.goal_state, self.current_state)
        else:
            return None  
   
    def goal_checking(self):
        if self.current_state == self.goal_state:
            print("Goal state has been reached! Stop")
            return True
        else:
            return False

    def display_state(self):
        for i in range(3):
            print(self.current_state[i * 3:i * 3 + 3])   

    def calculate_heuristic(self):
        return sum([1 if self.current_state[i] != self.goal_state[i] and self.current_state[i] != 0 else 0 for i in range(9)])

    def f(self):
        return self.g + self.h

    def get_best_move(self, open_list):
        best_move = None
        best_f_value = float('inf')
        for move in open_list:
            if move.f() < best_f_value:
                best_f_value = move.f()
                best_move = move
        return best_move

    def hill_climbing(self):
        open_list = [self]
        closed_list = []

        while open_list:
            #best move
            current = self.get_best_move(open_list)
            open_list.remove(current)
            closed_list.append(current)
#goal
            if current.goal_checking():
                return current

#neigbur
            successors = [current.up(), current.down(), current.left(), current.right()]

            for successor in successors:
                if successor is not None and successor not in closed_list:
                    if successor not in open_list or successor.g > current.g + 1:
                        successor.g = current.g + 1
                        successor.h = successor.calculate_heuristic()
                        successor.parent = current
                        open_list.append(successor)

        return None

def main():
    my_list = [2, 0, 3, 1, 8, 4, 7, 6, 5]  
    goal_list = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    p = Puzzle(my_list, goal_list)

    print("Initial State")
    p.display_state()

    result = p.hill_climbing()
    if result is not None:
        print("Goal state reached.")
    else:
        print("Failed to reach goal state.")
              
if __name__ == "__main__":
    main()
