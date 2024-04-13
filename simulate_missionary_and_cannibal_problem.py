#Problem : To simulate Missionary and cannibal problem statement using python programing language 

##analysis of the  flow chat of problem statement

#Start
#Is the initial state the final state?
#   Yes
#     Return the solution
#   No
# Generate all possible successor states
# Are any of the successor states the final state?
#   Yes
#     Return the solution
#   No
# Add all of the successor states to the queue
# Go to step 2")

class State:   #Using python class component
    def __init__(self, missionaries_left, missionaries_right, cannibals_left, cannibals_right, river_side): ##Initialiazing the object attribute 
        self.missionaries_left = missionaries_left   ## Pasiing a default parameter /arguement 
        self.missionaries_right = missionaries_right 
        self.cannibals_left = cannibals_left
        self.cannibals_right = cannibals_right
        self.river_side = river_side
        self.parent = None
        self.children = [] ##To return an  array of object after operation 

    def __str__(self):
        return (
            f"missionaries: {self.missionaries_left}\t| missionaries: {self.missionaries_right}\n"
            f"cannibals:: {self.cannibals_left}\t| cannibals: {self.cannibals_right}"
        ) ## Defining a  string method to return a readable format

    def is_valid_state(self):
        if self.missionaries_left < 0 or self.missionaries_right < 0 \
                or self.cannibals_left < 0 or self.cannibals_right < 0:
            return False

        return (self.missionaries_left == 0 or self.missionaries_left >= self.cannibals_left) and (
            self.missionaries_right == 0 or self.missionaries_right >= self.cannibals_right
        ) #Logic to define the valid state of initial objects movement 

    def is_final_state(self):
        return (
            self.missionaries_left == self.cannibals_left == 0
            and self.missionaries_right == self.cannibals_right == 3
        )  #Logic to define the valid state of final  objects movement

#Logic to determine the movement to distinguish the movement of cannibals and missionary  

    def generate_children(self):
        new_river_side = "right" if self.river_side == "left" else "left"

        moves = [
            {"missionaries": 2, "cannibals": 0},
            {"missionaries": 1, "cannibals": 0},
            {"missionaries": 1, "cannibals": 1},
            {"missionaries": 0, "cannibals": 1},
            {"missionaries": 0, "cannibals": 2},
        ] ## Defining the movement in with dictionary and a key

        for move in moves:
            if self.river_side == "left":
                missionaries_left = self.missionaries_left - move["missionaries"]
                missionaries_right = self.missionaries_right + move["missionaries"]
                cannibals_left = self.cannibals_left - move["cannibals"]
                cannibals_right = self.cannibals_right + move["cannibals"]
            else:
                missionaries_right = self.missionaries_right - move["missionaries"]
                missionaries_left = self.missionaries_left + move["missionaries"]
                cannibals_right = self.cannibals_right - move["cannibals"]
                cannibals_left = self.cannibals_left + move["cannibals"]

            child = State(missionaries_left, missionaries_right, cannibals_left, cannibals_right, new_river_side)
            child.parent = self
            if child.is_valid_state():
                self.children.append(child)

#Passing the state to generate a solution using a class component this approach used FIFO queing aproach to solve the cannibal systems 
class Solve:
    def __init__(self, state):
        self.queue = [state]
        self.solution = None

    def generate_solution(self):
        while self.queue:
            element = self.queue.pop(0)
            if element.is_final_state():
                self.solution = [element]
                while element.parent:
                    self.solution.insert(0, element.parent)
                    element = element.parent
                break

            element.generate_children()
            self.queue.extend(element.children)


def main():
    run = Solve(State(3, 0, 3, 0, "left"))
    run.generate_solution()

    for valid_state in run.solution:
        print(valid_state)
        print("************************************")


if __name__ == "__main__":
    main()
##Run the program