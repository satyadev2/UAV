class OmnidirectionalAntenna:
    def __init__(self, gain=2, frequency=2.4e9):
        self.gain = gain  # Gain in dBi
        self.frequency = frequency  # Frequency in Hz

    def get_signal_strength(self, distance):
        # Placeholder for signal strength calculation
        return self.gain / (distance ** 2)
