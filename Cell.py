class Cell:
    def __init__(self, name):
        self.name = name
        self.size = 1

    def grow(self):
        self.size += 1
    
    def status(self):
        if self.size<5:
            return f"{self.name} is a Small cell"
        else:
            return f"{self.name} is a Large cell"
            
    def __str__(self):
        return f"Name is {self.name} and Size is {self.size}"



name = input("Enter the Name: ")
times = int(input("Enter the No.of times cell should grow: "))

c1 = Cell(name)

for _ in range(times):
    c1.grow()
    
# print(c1.status())

print(c1)
