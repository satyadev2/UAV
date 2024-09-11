import matplotlib.pyplot as plt
import time
from ue0 import generate_random_users, move_users
from uav0 import place_uavs_greedy, UAV

# Simulation parameters
m, n = 10, 10  # Grid size
num_users = 100  # Number of users
coverage_radius = 2.5  # Coverage radius of each UAV
backhaul_range = 8.0  # Backhaul connection range between UAVs
time_steps = 10  # Number of time steps to simulate

# Function to visualize the grid, users, and UAV coverage
def visualize_grid(m, n, users, selected_uavs, coverage_radius, time_step):
    plt.figure(figsize=(10, 10))

    # Plot users
    for user in users:
        plt.plot(user.position[0], user.position[1], 'bo', label='User' if users.index(user) == 0 else "")

    # Plot UAV coverage
    for uav in selected_uavs:
        circle = plt.Circle(uav.position, uav.coverage_radius, color='r', alpha=0.3, label='UAV Coverage' if selected_uavs.index(uav) == 0 else "")
        plt.gca().add_patch(circle)
        plt.plot(uav.position[0], uav.position[1], 'rx', markersize=10, label='UAV Position' if selected_uavs.index(uav) == 0 else "")

    # Plot UAV backhaul connections
    for uav in selected_uavs:
        for connected_uav in uav.connected_uavs:
            plt.plot([uav.position[0], connected_uav.position[0]], [uav.position[1], connected_uav.position[1]], 'g--',
                     label='Backhaul Link' if uav == selected_uavs[0] and connected_uav == list(uav.connected_uavs)[0] else "")

    # Set plot limits and labels
    plt.xlim(0, m)
    plt.ylim(0, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.xlabel('Grid X')
    plt.ylabel('Grid Y')
    plt.title(f'UAV Coverage and Backhaul on Grid at Time Step {time_step}')
    plt.legend()
    plt.show()

# Generate random users with unique IDs
users = generate_random_users(m, n, num_users)

# Place UAVs using the greedy algorithm based on initial user distribution
selected_positions, covered_users = place_uavs_greedy(m, n, [user for user in users], coverage_radius)
uavs = [UAV(position=pos, coverage_radius=coverage_radius, backhaul_range=backhaul_range) for pos in selected_positions]

# Initial coverage and backhaul setup
for uav in uavs:
    uav.update_coverage(users)
    uav.update_backhaul_connections(uavs)

# Print initial coverage stats
print("Initial UAV placement:")
print(f"Covered users: {len(covered_users)}")
print(f"Coverage percentage: {len(covered_users) / num_users * 100:.2f}%\n")

# Initial visualization
visualize_grid(m, n, users, uavs, coverage_radius, time_step=0)

# Dynamic simulation loop
for t in range(1, time_steps + 1):
    move_users(users, m, n)  # Move users according to the mobility model

    # Update coverage and backhaul connections
    for uav in uavs:
        uav.update_coverage(users)
        uav.update_backhaul_connections(uavs)

    # Recalculate coverage
    covered_users = set()
    for uav in uavs:
        covered_users.update(uav.covered_users)

    # Print coverage stats
    print(f"Time Step {t}:")
    print(f"Covered users: {len(covered_users)}")
    print(f"Coverage percentage: {len(covered_users) / num_users * 100:.2f}%\n")

    # Print user details
    print("Users currently covered:")
    covered_user_ids = [user.id for user in covered_users]
    print(", ".join(covered_user_ids) if covered_user_ids else "No users covered.\n")

    # Visualize the current state
    visualize_grid(m, n, users, uavs, coverage_radius, time_step=t)

    time.sleep(1)  # Optional: Pause for visualization clarity
