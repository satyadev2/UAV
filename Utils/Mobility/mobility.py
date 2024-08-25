import numpy as np

class MobilityModel:
    def __init__(self, initial_position, speed):
        self.position = np.array(initial_position)
        self.speed = speed  # Speed in units per time step

    def move(self):
        # Example of a simple linear motion model
        direction = np.random.rand(2) - 0.5  # Random direction in 2D plane
        direction /= np.linalg.norm(direction)  # Normalize to unit vector
        self.position += self.speed * direction

    def get_position(self):
        return self.position
