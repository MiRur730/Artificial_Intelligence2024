class Puzzle(object):
    def __init__(self,initial_state,goal_state):
        self.current_state=initial_state
        self.goal=goal_state
        self.empty_state=self.find_empty()

    def find_empty(self):
        for i in range(9):
            if self.current_state[i]==0:

              return i 
    def  move_tile(self,index):
        temp=self.current_state[:]
        temp[self.empty_state]      = self.current_state[index]
        temp[index]=0
        self.empty_state=index
        return temp
    def up(self):
        if self.empty_state-3>=0:
            index=        self.empty_state-3
            temp =self.move_tile(index)
            return temp
        else :
            return None
    def down(self):
        if self.empty_state+3<9:
            index=        self.empty_state-3
            temp =self.move_tile(index)
            return temp 
        else :
            return None   
    def right(self):
        if (self.empty_state-1)%3!=0:
            index=        self.empty_state-3
            temp =self.move_tile(index)
            return temp
        else :
            return None
    def left(self):
        if self.empty_state%3!=0:
            index=        self.empty_state-3
            temp =self.move_tile(index)
            return temp  
        else :
            return None              
    def goal_find(self):
        if self.current_state==self.goal_state:
            return True
        else:
           return False
    def display(self):
        for i in range(3):
            print(self.current_state[i*3:i*3+3])
    def generate_neighbur(self,temp):
        self.current_state=temp
        ups=self.up()
        downs=self.down()
        rights=self.right()
        left=self.left()
        stack=[]
        new=[ups,downs,rights,left]
        for n in new:
            if n is not None:
                stack.append(n)
        return stack
    def dfs(self,open_list,closed_list,depth):

        
        stack=[(self.current_state,0)]
        isVisited=set()
        isVisited.add(tuple(self.current_state))
        

        while stack:
            temp,d=stack.pop()
            closed_list.add(tuple(temp))
            if temp==self.goal_state:
                return True
            
            if d< depth:

             neigh=self.generate_neighbur(temp)
             for n in neigh:
              if tuple(n) in isVisited and tuple(n) not in closed_list and tuple(n) not in open_list:
                 stack.append(n,d+1)
                 open_list.add(tuple(n))
                 closed_list.add(tuple(n))

        return False

    def idf(self):
        depth=0
        open_list=set()
        closed_list=set()
        while True:
            if self.dfs(open_list,closed_list,depth):
                return True
            else:
                depth+=1
                
def main():
    my_list=[]
    goal_list=[]
    p=Puzzle(my_list,goal_list)

    p.idf()
if __name__=="__main__":
    main()
    