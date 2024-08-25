class UE:
    def __init__(self, id, position, mobility_model=None):
        self.id = id
        self.position = np.array(position)
        self.mobility_model = mobility_model

    def update_position(self):
        if self.mobility_model:
            self.mobility_model.move()
            self.position = self.mobility_model.get_position()
    
    def get_position(self):
        return self.position

    def connect_to_uav(self, uav):
        distance = np.linalg.norm(self.position - uav.position)
        signal_strength = uav.omnidirectional_antenna.get_signal_strength(distance)
        return signal_strength

# Example usage:

# Creating UEs with and without mobility models
static_ue = UE(id=1, position=[50, 50, 0])
moving_ue = UE(id=2, position=[0, 0, 0], mobility_model=MobilityModel(initial_position=[0, 0, 0], speed=1))

uav = UAV(id=1, position=[0, 0, 100], beamforming_antenna=BeamformingAntenna(), omnidirectional_antenna=OmnidirectionalAntenna())

# Simulate for a few time steps
for _ in range(10):
    moving_ue.update_position()
    print(f"Static UE Position: {static_ue.get_position()}")
    print(f"Moving UE Position: {moving_ue.get_position()}")
    print(f"Signal strength to static UE: {static_ue.connect_to_uav(uav)}")
    print(f"Signal strength to moving UE: {moving_ue.connect_to_uav(uav)}")
