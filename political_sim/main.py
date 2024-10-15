# Policy Sim
#
# -- Things to add
# 1. Policy for each entity, this will be some values to follow depending on the political ideology
# 2. Conversion of ideology.
# 3.


import random as rand
from setup.grid import Grid
from entities.entity import Entity

GRID_WIDTH = 50
GRID_HEIGHT = 50
START_RESOURCE_COUNT = 20

def grid_setup() -> list[list]:
    grid_space = Grid(sizex=GRID_WIDTH, sizey=GRID_HEIGHT)
    grid_space.generate_resource(num_nodes=START_RESOURCE_COUNT)

    return grid_space


def simulation_step(entities: list[object], grid) -> str:
    for entity in entities:
        entity.action()


if __name__ == "__main__":

    main_grid = grid_setup()
    main_grid.show_grid()



