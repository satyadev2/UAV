import numpy as np

class UAV:
    def __init__(self, id, position, beamforming_antenna, omnidirectional_antenna):
        self.id = id
        self.position = np.array(position)
        self.beamforming_antenna = beamforming_antenna
        self.omnidirectional_antenna = omnidirectional_antenna

    def connect_to_uav(self, other_uav, angle_offset=0):
        distance = np.linalg.norm(self.position - other_uav.position)
        link_quality = self.beamforming_antenna.get_link_quality(distance, angle_offset)
        return link_quality

    def connect_to_ground_user(self, ground_user_position):
        distance = np.linalg.norm(self.position - np.array(ground_user_position))
        signal_strength = self.omnidirectional_antenna.get_signal_strength(distance)
        return signal_strength

    def move(self, new_position):
        self.position = np.array(new_position)
    


# Example usage:
beamforming_antenna = BeamformingAntenna(gain=12, beamwidth=25, frequency=26e9)
omnidirectional_antenna = OmnidirectionalAntenna(gain=3, frequency=2.4e9)

uav1 = UAV(id=1, position=[0, 0, 100], beamforming_antenna=beamforming_antenna, omnidirectional_antenna=omnidirectional_antenna)
uav2 = UAV(id=2, position=[100, 0, 100], beamforming_antenna=beamforming_antenna, omnidirectional_antenna=omnidirectional_antenna)

link_quality = uav1.connect_to_uav(uav2, angle_offset=10)
print(f"Link quality between UAV1 and UAV2: {link_quality}")

signal_strength = uav1.connect_to_ground_user([50, 50, 0])
print(f"Signal strength from UAV1 to ground user: {signal_strength}")
