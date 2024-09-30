# Policy Sim
#
# -- Things to add
# 1. Policy for each entity, this will be some values to follow depending on the political ideology
# 2. Conversion of ideology.
# 3.   


class Entity:
    def __init__(self, policy, political_confidence = 100):
        self.policy = policy
        self.political_confidence = 100
        self.alive = True # Used to terminate activity
        self.active = False # Used to set starting point
        self.position_x = 0 
        self.position_y = 0
        self.position = [self.position_x, self.position_y]


    def __str__(self) -> str:

        position = [self.position_x, self.position_y]
        
        status = f"Alive: {self.alive}, Political Confidence: {self.political_confidence}, Position: {position}"
        
        return status

    def action(self):
        return None

    def set_start(self, grid):
        # Set the starting location for the node, cannot be in an occupied space
        return 0, 0
    

class Grid:
    def __init__(self, sizex: int, sizey: int):
        self.sizex = sizex
        self.sizey = sizey
        self.grid = self.create_grid()

    def create_grid(self):

        x = range(self.sizex)
        y = range(self.sizey)

        grid = [[0 for col in x] for row in y]

        return grid
    
    def show_grid(self):
        for col in self.grid:
            print(col)

    def update(self, entity_positions):
        for entity, position in entity_positions.items():
            
            x = position[0]
            y = position[1]

            self.grid[x][y] = entity

def simulation_step(entities: list[object], grid) -> str:
    for entity in entities:
        entity.action()



if __name__ == "__main__":
    grid1 = Grid(10, 10)
    grid1.show_grid()

    entity1 = Entity(policy=None)
    position = entity1.position

    entity_position = {entity1: position}

    grid1.update(entity_position)
    grid1.show_grid()

    print(grid1.grid[0][0])
