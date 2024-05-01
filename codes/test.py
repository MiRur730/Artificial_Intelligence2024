#Apply Steepest Hill Climbing with “Number of correctly placed tiles
#as heuristic and display the solution


class Puzzle(object):
    
    def __init__(self, initial_state, goal_state,parent=None):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.empty_tile = self.get_empty_index()
        self.parent = parent


    def get_empty_index(self):
        index=[]
        for i in range(9):
            if self.current_state[i] == 0:
                index.append(i)
        return index   
            # index for the empty tile    
    
    def move_empty_tile(self, new_empty_index):
        temp_state=self.current_state[:]
        temp_state[self.empty_tile]=temp_state[new_empty_index]
        temp_state[new_empty_index] = 0
        self.empty_tile = new_empty_index
        return temp_state
    
    def move_empty_tiles(self, new_empty_indices):
        temp_state = self.current_state[:]
        for i in range(len(self.empty_tiles)):
            temp_state[self.empty_tiles[i]] = temp_state[new_empty_indices[i]]
            temp_state[new_empty_indices[i]] = 0
        self.empty_tiles = new_empty_indices
        return temp_state

    def down(self):
        self.empty_tile = self.get_empty_index()
        if self.empty_tile + 3 < 9:
            new_empty_index = self.empty_tile + 3
            temp = self.move_empty_tile(new_empty_index)
             
            return Puzzle(temp, self.goal_state,self.current_state)
        else:
            return None 
       
    def up(self):
        self.empty_tile = self.get_empty_index()
        if self.empty_tile - 3 >= 0:
            new_empty_index = self.empty_tile - 3
            temp= self.move_empty_tile(new_empty_index)
            return Puzzle(temp, self.goal_state,self.current_state)
        else:
            return None

    def right(self):
        self.empty_tile = self.get_empty_index()
        print(self.empty_tile )
        if (self.empty_tile + 1) % 3 != 0:
            new_empty_index = self.empty_tile + 1 
            temp= self.move_empty_tile(new_empty_index)
            
            return Puzzle(temp, self.goal_state,self.current_state)
        else:
            return None

    def left(self):
        self.empty_tile = self.get_empty_index()
        if self.empty_tile % 3 != 0:
            new_empty_index = self.empty_tile - 1
            temp= self.move_empty_tile(new_empty_index)
            
            return Puzzle(temp, self.goal_state,self.current_state)
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
    #correctly placed 
      return sum([1 if self.current_state[i] == self.goal_state[i] and self.current_state[i] != 0 else 0 for i in range(9)])

    

     
            #move either up down left right insequence whichever has lowest hf than parent 
    def steepest_hill_climbing(self):


        while True:
            parent=self
            if self.current_state==self.goal_state:
                print("Goal state has been reached !Stop")
                break
            
            heuristic=self.calculate_heuristic()
            best_move=None
            print(heuristic)
            
            up_s=parent.up()

            if up_s is not None:
                
                
                print(up_s.current_state)
                h1= up_s.calculate_heuristic()
                print(h1)
                if h1 < heuristic:
                     heuristic=h1
                     best_move=up_s 

            down_s=parent.down()
            
            if down_s is not None:
                
                print(down_s.current_state)
                h2= down_s.calculate_heuristic()
                print(h2)
                if h2 < heuristic:
                     heuristic=h2
                     best_move=down_s



            right_s=parent.right()
            
            if right_s is not None:
                print(right_s.current_state)
                h3= right_s.calculate_heuristic()
                print(h3)
                if h3<heuristic:
                  heuristic=h3
                  best_move=right_s
            left_s=parent.left()    

            if left_s is not None:
                h4= left_s.calculate_heuristic()
                print(h4) 

                if h4<heuristic:
                  heuristic=h4
                  best_move=left_s
                  
            
            if best_move is None :
             print("Cannot improve heuristic. Stopping.")
             break
              

            self.current_state=best_move.current_state 
            self.empty_tile = best_move.empty_tile
            self.display_state()
            

def main():
    my_list = [0,3,6,1,2,0,4,5,7]  
    goal_list = [1,2,3,4,5,6,7,0,0]

    p = Puzzle(my_list, goal_list)

    print("Initial State")
    p.display_state()

    p.steepest_hill_climbing()
              
if __name__ == "__main__":
    main()
