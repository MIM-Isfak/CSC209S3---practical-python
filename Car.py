class Car:
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed
        
    def increaseSpeed(self):
        self.speed += 10
        
    def getColor(self):
        return self.color
    
    def __str__(self):
        return f"Car color is {self.color} and speed is {self.speed}."
        
class AudiCar(Car):
    # def getSpeed(self):
        # return self.speed
    pass    
    
        
c1 = Car("Blue", 350)
c2 = AudiCar("Green", 100)
c2.increaseSpeed()

print(c1.getColor())
print(c1)

print(c2)