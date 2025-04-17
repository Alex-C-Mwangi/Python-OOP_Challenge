class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.available_tricks = ['Sit', 'Roll over', 'Shake', 'Jump']
    def _clamp(self, value):
        return max(0, min(10, value))
    def eat(self):
        self.hunger = self._clamp(self.hunger -3)
        self.happiness = self._clamp(self.happiness +1)
        print(f"{self.name} has been fed")
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
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} has learned how to {trick}")
        else:
            print(f"{self.name}already knows how to{trick}")
            return
        if self.energy < 1:
            print(f"{self.name} is too tired to learn new tricks!")
            return
        self.energy = self._clamp(self.energy -1)
        self.happiness = self._clamp(self.happiness + 1)
        print(f"{self.name} learned how to {trick}!")
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks")