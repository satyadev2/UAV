# simulation.py

import random
import time
import matplotlib.pyplot as plt
from uav import UAV
from ue import User

def generate_random_users(m, n, num_users):
    return [User(i, random.uniform(0, m), random.uniform(0, n)) for i in range(num_users)]

def visualize_grid(m, n, users, uavs, coverage_radius, time_step):
    plt.figure(figsize=(10, 10))
    
    for user in users:
        plt.plot(user.position[0], user.position[1], 'bo', label='User' if users.index(user) == 0 else "")

    for uav in uavs:
        circle = plt.Circle(uav.position, coverage_radius, color='r', alpha=0.3, label='UAV Coverage' if uavs.index(uav) == 0 else "")
        plt.gca().add_patch(circle)
        plt.plot(uav.position[0], uav.position[1], 'rx', markersize=10, label='UAV Position' if uavs.index(uav) == 0 else "")
    
    plt.xlim(0, m)
    plt.ylim(0, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.xlabel('Grid X')
    plt.ylabel('Grid Y')
    plt.title(f'UAV Network at Time Step {time_step}')
    plt.legend()
    plt.show()

def place_uavs(m, n, users, coverage_radius, num_uavs=5):
    uavs = []
    for i in range(num_uavs):
        x = random.uniform(0, m)
        y = random.uniform(0, n)
        uav = UAV(i, x, y, coverage_radius)
        uav.update_coverage(users)
        uavs.append(uav)
    return uavs

# Simulation parameters
m, n = 10, 10  # Grid size
num_users = 100  # Number of users
coverage_radius = 2.5  # Coverage radius of each UAV
time_steps = 10  # Number of time steps to simulate

users = generate_random_users(m, n, num_users)
uavs = place_uavs(m, n, users, coverage_radius)

# Initial visualization
visualize_grid(m, n, users, uavs, coverage_radius, time_step=0)

# Simulation loop
for t in range(1, time_steps + 1):
    for user in users:
        user.move(m, n)

    for uav in uavs:
        uav.update_coverage(users)
    
    print(f"Time Step {t}:")
    for uav in uavs:
        print(f"{uav}: Covered users = {len(uav.covered_users)}")
    
    visualize_grid(m, n, users, uavs, coverage_radius, time_step=t)
    time.sleep(1)
