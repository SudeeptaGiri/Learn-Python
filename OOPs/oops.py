class Car:

    def __init__(self, make, mode, year, color):
        self.make = make
        self.mode = mode
        self.year = year
        self.color = color

    def drive(self):
        print("Car is Driving")

    def start(self):
        print(self)

    def stop(self):
        print("Stop")
