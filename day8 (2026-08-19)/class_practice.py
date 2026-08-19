class Car:
    def __init__(self, color, speed, type):
        self.color = color
        self.speed = speed
        self.type = type

    def getColor(self):
        return self.color

    def calculateTime(self, distance):
        return distance / self.speed


audi = Car("red", 120, "XX1")

print(audi.getColor())          
print(audi.calculateTime(240))