class Car:
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.location = 0

    def printTopSpeed(self):
        print(f"Top speed: {self.top_speed} mph")
        
    def drive(self):
        self.location +=10
        print(f"The car has driven {self.location} miles from the start point.")
        
    def stop(self):
        print(f"Your final location is {self.location} miles from your start point.")


car1 = Car(150)
car1.printTopSpeed()

car1.drive()
car1.drive()
car1.drive()
car1.stop()
