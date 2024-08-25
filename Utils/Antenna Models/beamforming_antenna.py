class BeamformingAntenna:
    def __init__(self, gain=10, beamwidth=30, frequency=28e9):
        self.gain = gain  # Gain in dBi
        self.beamwidth = beamwidth  # Beamwidth in degrees
        self.frequency = frequency  # Frequency in Hz

    def get_link_quality(self, distance, angle_offset):
        # Placeholder for link quality calculation considering beamforming effects
        if angle_offset < self.beamwidth / 2:
            return self.gain / (distance ** 2)
        else:
            # Signal degradation outside beamwidth
            return (self.gain / (distance ** 2)) * (self.beamwidth / angle_offset)
