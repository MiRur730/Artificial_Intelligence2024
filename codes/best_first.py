from queue import PriorityQueue

class Puzzle(object):
    
    def __init__(self, initial_state, goal_state,parent=None):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.empty_tile = self.get_empty_index()
        self.parent = parent


    def get_empty_index(self):
        for i in range(9):
            if self.current_state[i] == 0:
                return i   
            # index for the empty tile    
    
    def move_empty_tile(self, new_empty_index):
        temp_state=self.current_state[:]
        temp_state[self.empty_tile]=temp_state[new_empty_index]
        temp_state[new_empty_index] = 0
        self.empty_tile = new_empty_index
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
    # Heuristic function: Number of misplaced tiles except 0 tile
      return sum([1 if self.current_state[i] != self.goal_state[i] and self.current_state[i] != 0 else 0 for i in range(9)])

    

    #heuristic function missing tiles 
            #move either up down left right insequence whichever has lowest hf than parent 
    def best_first(self):
        queue= PriorityQueue()  
        queue.put((self.calculate_heuristic(),self))
        
        while queue:
            

            

            _, top = queue.get()
            heuristic=top.calculate_heuristic()

            if top.current_state==self.goal_state:
                print("Goal state has been reached !Stop")
                break
            
           
            
            
            up_s=top.up()
            if up_s is not None:
                h1= up_s.calculate_heuristic()
                if h1 < heuristic:
                     
                    queue.put((h1,up_s))
            down_s=top.down()
            
            if down_s is not None:
                h2= down_s.calculate_heuristic()
                
                if h2 < heuristic:
                     
                     queue.put((h2,down_s))



            right_s=top.right()
            
            if right_s is not None:
                
                h3= right_s.calculate_heuristic()
                
                if h3<heuristic:
                  heuristic=h3
                  queue.put((h3,right_s))

            left_s=top.left()    

            if left_s is not None:
                h4= left_s.calculate_heuristic()
               
                if h4<heuristic:
                  queue.put((h4,left_s))
                  
            
            
              

           
            

def main():
    my_list = [2,0,3,1,8,4,7,6,5]
    goal_list = [1,2,3,8,0,4,7,6,5]

    p = Puzzle(my_list, goal_list)

    print("Initial State")
    p.display_state()

    p.best_first()
              
if __name__ == "__main__":
    main()

