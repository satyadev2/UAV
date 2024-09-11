import random

class User:
    def __init__(self, position, user_id):
        self.position = position
        self.id = user_id

def generate_random_users(m, n, num_users):
    """Generate random users with unique IDs on the grid."""
    users = []
    for i in range(num_users):
        position = (random.uniform(0, m), random.uniform(0, n))
        user = User(position=position, user_id=f"U{i+1}")
        users.append(user)
    return users

def move_users(users, m, n):
    """Move users randomly within the grid bounds."""
    for user in users:
        new_x = max(0, min(m, user.position[0] + random.uniform(-1, 1)))
        new_y = max(0, min(n, user.position[1] + random.uniform(-1, 1)))
        user.position = (new_x, new_y)
