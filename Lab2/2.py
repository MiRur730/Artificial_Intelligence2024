class Jug:
    def _init_(self, capacity):
        self.capacity = capacity
        self.current = 0

    def fill(self):
        self.current = self.capacity

    def empty(self):
        self.current = 0

    def pour_into(self, other_jug):
        if other_jug.current + self.current <= other_jug.capacity:
            other_jug.current += self.current
            self.empty()
        else:
            self.current -= other_jug.capacity - other_jug.current
            other_jug.current = other_jug.capacity

    def is_full(self):
        return self.current == self.capacity

    def is_empty(self):
        return self.current == 0


def simulate_fill(jug3, jug4):
    jug3.fill()  # Step 1
    jug3.pour_into(jug4)  # Step 2
    jug3.empty()  # Step 3
    jug4.pour_into(jug3)  # Step 4
    jug3.fill()  
    while not jug4.is_full() and not jug3.is_empty():
        jug3.pour_into(jug4)     
    if jug4.current != 2:  
        jug3.pour_into(jug4)  

def main():
    jug3 = Jug(3)
    jug4 = Jug(4)
    simulate_fill(jug3, jug4)
    print("Final state of the jugs:")
    print("3-Liter Jug:", jug3.current, "liters")
    print("4-Liter Jug:", jug4.current, "liters")


if __name__ == "_main_":
    main()