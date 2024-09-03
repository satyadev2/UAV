import random
import math
import matplotlib.pyplot as plt
import time
import random

# User Class
class User:
    def __init__(self, position):
        self.position = position  # position is a list [x, y]
        self.connected_uav = None

    def connect_to_uav(self, uav):
        self.connected_uav = uav

# Function to generate random user objects
def generate_random_users(m, n, num_users):
    users = []
    for _ in range(num_users):
        x = random.uniform(0, m)
        y = random.uniform(0, n)
        users.append(User([x, y]))  # Create User objects
    return users


# ue0.py (continued)

# Function to simulate random walk for users
def move_users(users, m, n, step_size=0.5):
    for user in users:
        # Update x and y positions
        user.position[0] += random.uniform(-step_size, step_size)
        user.position[1] += random.uniform(-step_size, step_size)
        
        # Ensure users stay within grid boundaries
        user.position[0] = max(0, min(user.position[0], m))
        user.position[1] = max(0, min(user.position[1], n))
