class Puzzle(object):
    
    def __init__(self, initial_state, goal_state):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.empty_tile = self.get_empty_index()
        # self.parent = None


    def get_empty_index(self):
        for i in range(9):
            if self.current_state[i] == 0:
                return i   
            # index for the empty tile    
    
    def move_empty_tile(self, new_empty_index):
        temp_state=self.current_state[:]
        temp_state[self.empty_tile]=temp_state[new_empty_index]
        temp_state[new_empty_index] = 0
        # self.current_state=temp_state
        self.empty_tile = new_empty_index
        return temp_state

    

    # def down(self):
    #     if self.empty_tile + 3 < 9:
    #         new_empty_index = self.empty_tile + 3
    #         return  self.move_empty_tile(new_empty_index)
    #     # this will not work 
    #     #as current state ko bhi btana hai
    #     else:
    #         return None
        


    def down(self):
        if self.empty_tile + 3 < 9:
            new_empty_index = self.empty_tile + 3
            self.current_state = self.move_empty_tile(new_empty_index)
             
            return self.current_state
        else:
            return None 
       
    def up(self):
        if self.empty_tile - 3 >= 0:
            new_empty_index = self.empty_tile - 3
            self.current_state= self.move_empty_tile(new_empty_index)
            return self.current_state
        else:
            return None

    def right(self):
        if (self.empty_tile + 1) % 3 != 0:
            new_empty_index = self.empty_tile + 1 
            # this is giving new index for 
            self.current_state= self.move_empty_tile(new_empty_index)
            return self.current_state
        else:
            return None

    def left(self):
        if self.empty_tile % 3 != 0:
            new_empty_index = self.empty_tile - 1
            self.current_state= self.move_empty_tile(new_empty_index)
            return self.current_state
        else:
            return None  


       
           
   
             
    def goal_checking(self):
        if self.current_state==self.goal_state:
          print("Goal state has been reached !Stop")
          return True

    def display_state(self):
        for i in range(3):
            print(self.current_state[i * 3:i * 3 + 3])   

 
    

            
def main():
    my_list = [1, 2, 3, 0, 4, 6, 7, 8, 9]
    goal_list = [1, 2, 3, 4, 0, 6, 7, 8, 9]

    p = Puzzle(my_list, goal_list)

    print("Initial State")
    p.display_state()

    # print(" moving down:")
    # p.down()
    # p.display_state()

    while True:
        print("PICK 1 FOR DOWN , 2FOR UP, 3 RIGHT ,4 LEFT")
        ans=int(input())

        if ans==1:
            p.down()
        elif ans==2:
            p.up()
        elif ans==3:
            p.right()        
        elif ans==4:
            p.left()
        else:
            print("INVALID INPUT")  
            continue  
        p.display_state()
        if p.goal_checking():
            break
              
if __name__ == "__main__":
    main()








# def main():
#     # Define initial and goal states
#     initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
#     goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

#     # Create puzzle object
#     puzzle = Puzzle(initial_state, goal_state)

#     # Display initial state
#     print("Initial State:")
#     puzzle.display_state()

#     # Move down
#     print("\nMoving down:")
#     new_state_down = puzzle.down()
#     if new_state_down:
#         puzzle.current_state = new_state_down
#         puzzle.empty_tile = puzzle.get_empty_index()
#         puzzle.display_state()
#     else:
#         print("Invalid move: Cannot move down")

#     # Move up
#     print("\nMoving up:")
#     new_state_up = puzzle.up()
#     if new_state_up:
#         puzzle.current_state = new_state_up
#         puzzle.empty_tile = puzzle.get_empty_index()
#         puzzle.display_state()
#     else:
#         print("Invalid move: Cannot move up")

# if __name__ == "__main__":
#     main()

                   

