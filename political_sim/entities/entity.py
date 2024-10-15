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
    