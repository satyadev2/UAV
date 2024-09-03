# user.py

import random

class User:
    def __init__(self, id, x, y):
        self.id = id
        self.position = [x, y]

    def move(self, m, n, step_size=0.5):
        self.position[0] += random.uniform(-step_size, step_size)
        self.position[1] += random.uniform(-step_size, step_size)
        self.position[0] = max(0, min(self.position[0], m))
        self.position[1] = max(0, min(self.position[1], n))

    def __repr__(self):
        return f'User-{self.id} at {self.position}'
