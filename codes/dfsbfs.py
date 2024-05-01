

class Puzzle(object):
    
    def __init__(self, initial_state, goal_state):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.empty_tile = self.get_empty_index()
        # self.parent = None
    
    def move_empty_tile(self, new_empty_index):
        temp_state=self.current_state[:]
        temp_state[self.empty_tile]=temp_state[new_empty_index]
        temp_state[new_empty_index] = 0
        # self.current_state=temp_state
        return temp_state

    

    def down(self):
        if self.empty_tile + 3 < 9:
            new_empty_index = self.empty_tile + 3
            return  self.move_empty_tile(new_empty_index)
        # this will not work 
        #as current state ko bhi btana hai becoz 
    
        else:
            return None
        


    def new_down(self):
        if self.empty_tile + 3 < 9:
            new_empty_index = self.empty_tile + 3
            temp = self.move_empty_tile(new_empty_index)
             
            return temp
        else:
            return None 
        



     # self.empty_tile = new_empty_index    
    def up(self):
        if self.empty_tile - 3 >= 0:
            new_empty_index = self.empty_tile - 3
            temp= self.move_empty_tile(new_empty_index)

            return temp
        else:
            return None

    def right(self):
        if (self.empty_tile + 1) % 3 != 0:
            new_empty_index = self.empty_tile + 1 
            # this is giving new index for 
            temp= self.move_empty_tile(new_empty_index)
            return temp
        else:
            return None

    def left(self):
        if self.empty_tile % 3 != 0:
            new_empty_index = self.empty_tile - 1
            temp= self.move_empty_tile(new_empty_index)
            return temp
        else:
            return None  


       
           
    def get_empty_index(self):
        for i in range(9):
            if self.current_state[i] == 0:
                return i   
            # index for the empty tile
             
    def goal_checking(self):
        if self.current_state==self.goal_state:
          print("Goal state has been reached !Stop")

    def display_state(self):
        for i in range(3):
            print(self.current_state[i * 3:i * 3 + 3])   

    def generate_neburs(self,temp_state):
        self.current_state = temp_state
        nebour = []

        
        up_s = self.up()
        print(up_s)
        if up_s is not None:
            nebour.append((up_s))

        
        down_s = self.new_down()
        print("Down")
        print(down_s)
        if down_s is not None:
            nebour.append((down_s))

    
        left_s = self.left()
        print("Left")
        print(left_s)
        if left_s is not None:
            nebour.append((left_s))

        
        right_s = self.right()
        print("Right")
        print(right_s)
        if right_s is not None:
            nebour.append((right_s))

        return nebour
    
    def bfs(self):
        print("Entered bfs")
        queue=[]
        Visited=set()
        Visited.add(tuple(self.current_state))
        queue.append(self.current_state)



        while queue:
           temp=queue.pop(0)
        #    print(temp)
        #    print(" \n")
           if temp == self.goal_state:
             print("Goal state has been reached!")
             return  
           list = self.generate_neburs(temp)
          


           for i in range(len(list)):
            #    tuple nikalana
               if tuple(list[i]) not in Visited:

                queue.append(list[i])
                Visited.add(tuple(list[i]))
        
    def dfs(self):
        stack=[]
        stack.append(self.current_state)
        isVisited=set()
        isVisited.add(tuple(self.current_state))
        while stack:
            print("Top State in stack is")
            temp=stack.pop()
            print(temp)
            if(temp == self.goal_state):
                print("State has been Reached")
                return
                
            list=self.generate_neburs(temp)
            
            for i in range(len(list)):
                if tuple(list[i]) not in isVisited:
                    stack.append(list[i])
                    isVisited.add(tuple(list[i]))
                    



               
def main():
    my_list = [1, 2, 3, 0, 4, 6, 7, 8, 9]
    goal_list = [1, 2, 3, 4, 0, 6, 7, 8, 9]

    # p = Puzzle(my_list, goal_list)

    # print("Initial State:")
    # p.display_state()

    # print("\nBFS:")
    # p.bfs()

    print("\nDFS:")
    p = Puzzle(my_list, goal_list)  # Reset the puzzle
    p.dfs()


if __name__ == "__main__":
    main()

