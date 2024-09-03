# uav.py

import math

class UAV:
    def __init__(self, id, x, y, coverage_radius):
        self.id = id
        self.position = [x, y]
        self.coverage_radius = coverage_radius
        self.connected_uavs = []  # Backhaul connections
        self.covered_users = set()  # Users served by this UAV (fronthaul)

    def distance(self, other_position):
        return math.sqrt((self.position[0] - other_position[0])**2 + (self.position[1] - other_position[1])**2)

    def add_backhaul_connection(self, uav):
        self.connected_uavs.append(uav)

    def cover_user(self, user):
        if self.distance(user.position) <= self.coverage_radius:
            self.covered_users.add(user)

    def update_coverage(self, users):
        self.covered_users.clear()
        for user in users:
            self.cover_user(user)

    def __repr__(self):
        return f'UAV-{self.id} at {self.position}'
