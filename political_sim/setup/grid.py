import random as rand

class Grid:
    def __init__(self, sizex: int, sizey: int):
        self.sizex = sizex
        self.sizey = sizey
        self.grid = self.create_grid()

    def create_grid(self):

        x = range(self.sizex)
        y = range(self.sizey)

        grid = [['_' for col in x] for row in y]

        return grid
    
    def show_grid(self):
        for col in self.grid:
            print(col)

    def update(self, entity_positions):
        for entity, position in entity_positions.items():
            
            x = position[0]
            y = position[1]

            self.grid[x][y] = entity

    def generate_resource(self, num_nodes: int) -> None:

        while num_nodes != 0:
            
            loc_x = rand.randint(0, self.sizex-1)
            loc_y = rand.randint(0, self.sizey-1)
            
            print(loc_x, " ", loc_y)
            
            loc_status = self.grid[loc_y][loc_x]

            print(loc_status)

            if loc_status == '_':
                self.grid[loc_y][loc_x] = 'R'
                num_nodes -= 1