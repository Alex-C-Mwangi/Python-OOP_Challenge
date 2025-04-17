class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
    def _clamp(self, value):
        return max(0, min(10, value))
    def eat(self):
        self.hunger = self._clamp(self.hunger -3)
        self.happiness = self._clamp(self.happiness +1)
    def sleep(self):
        self.energy = self._clamp(self.energy +5)
        print(f"{self.name} is sleeping and feels energized")
    def play(self):
        self.energy = self._clamp(self.energy -2)
        self.happiness = self._clamp(self.happiness +2) 
        self.hunger = self._clamp(self.hunger +1)
        print(f"{self.name} is playing")
    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")