class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def swim(self):
        print("Moving in the water")


nemo = Fish()
nemo.swim()
nemo.breathe()