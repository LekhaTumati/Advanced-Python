class Rectangle:
    def __init__(self,c,l,w):
        self.colour = c
        self.length = l
        self.width = w
    
    def area(self):
        self.area = self.length*self.width
        return self.area

    def perimeter(self):
        self.perimeter = 2*(self.length + self.width)
        return self.perimeter
    
    def diagonal(self):
        self.diagonal = (self.width**2 + self.length**2)**(1/2)
        return self.diagonal

    def volume(self, h):
        self.height = h
        self.volume = self.length * self.width * self.height
        return self.volume

myRect1 = Rectangle('red', 2, 1)
myRect2 = Rectangle('blue', 4, 2)
print(myRect1.colour)
print("myRect1 length = " , myRect1.length)
print('myRect1 Area =' , myRect1.area())
print("myRect1 perimeter = " , myRect1.perimeter())
print("myRect1 Diagonal = ", myRect1.diagonal())
myVol = myRect1.volume(5)
print('myRect1 Volume = ', myVol)

print(myRect2.colour)
print("myRect2 length = " , myRect2.length)
print('myRect2 Area =' , myRect2.area())
print("myRect2 perimeter = " , myRect2.perimeter())
print("myRect2 Diagonal = ", myRect2.diagonal())
myVol1 = myRect2.volume(10)
print('myRect2 Volume = ', myVol1)