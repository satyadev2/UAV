import random
import math
import matplotlib.pyplot as plt
import time

# uav0.py (continued)

class UAV:
    def __init__(self, position, coverage_radius, backhaul_range):
        self.position = position  # [x, y]
        self.coverage_radius = coverage_radius
        self.backhaul_range = backhaul_range
        self.covered_users = set()       # Set of User objects
        self.connected_uavs = set()      # Set of UAV objects

    def update_coverage(self, users):
        self.covered_users = set()
        for user in users:
            if distance(self.position, user.position) <= self.coverage_radius:
                self.covered_users.add(user)
                user.connect_to_uav(self)

    def update_backhaul_connections(self, uavs):
        potential_connections = []
        for uav in uavs:
            if uav != self and distance(self.position, uav.position) <= self.backhaul_range:
                potential_connections.append(uav)

        # Sort potential connections by distance (closest first)
        potential_connections.sort(key=lambda uav: distance(self.position, uav.position))

        # Connect to the closest UAVs, with a maximum of 3 connections
        self.connected_uavs = set(potential_connections[:3])

    def print_statistics(self):
        print(f"UAV Position: {self.position}")
        print(f"Number of Covered Users: {len(self.covered_users)}")
        print(f"Covered Users' Positions: {[user.position for user in self.covered_users]}")
        print(f"Connected UAVs: {[uav.position for uav in self.connected_uavs]}")
        print("--------")




# Function to calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to find users covered by a UAV at a given position
def users_covered_by_uav(uav_pos, users, coverage_radius):
    covered_users = []
    for user in users:
        if distance(uav_pos, user.position) <= coverage_radius:
            covered_users.append(user)  # Append User objects
    return covered_users


def place_uavs_greedy(m, n, users, coverage_radius, coverage_threshold=0.9):
    uav_positions = [(i, j) for i in range(m) for j in range(n)]
    selected_uavs = []
    covered_users = set()
    total_users = len(users)
    required_coverage = coverage_threshold * total_users

    uav_cover_dict = []
    
    while len(covered_users) < required_coverage:
        best_uav = None
        best_covered_users = set()

        for uav_pos in uav_positions:
            current_covered_users = set(users_covered_by_uav(uav_pos, users, coverage_radius))
            new_covered_users = current_covered_users - covered_users

            penalty = 0

            if len(uav_cover_dict) >= 0:
                for cov_users in uav_cover_dict:
                    penalty += len(cov_users) -  len(cov_users - best_covered_users)

            penalty = 0.3 * penalty    
            
            if len(new_covered_users) > len(best_covered_users):
                best_uav = uav_pos
                best_covered_users = new_covered_users

        if best_uav is None:
            break

        selected_uavs.append(best_uav)
        covered_users.update(best_covered_users)
        uav_positions.remove(best_uav)
        uav_cover_dict.append(best_covered_users)
    
    return selected_uavs, covered_users

