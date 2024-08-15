class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("move")

    def draw(self):
        print("print")

    def dis(self,Point2):
        return (self.x-Point2.x)*(self.x-Point2.x)+(self.y-Point2.y)*(self.y-Point2.y)

class Person:
    def __init__(self, Name):
        self.Name = Name
        self.alive = True
        self.killer = ''

    def talk(self, text):
        print(self.Name + ' says: ' + text)

    def lives(self):
        return self.alive

    def kill(self, victim):
        victim.alive = False
        victim.killer = self.Name

point1 = Point(10,20)
point2 = Point(2,2)
print(point1.dis(point2))
print(point1.x)

Kai = Person('Kai')
Guenther = Person('Guenther')

Kai.talk('shut the fuck up')
print(Guenther.alive)
Kai.kill(Guenther)
print(Guenther.killer)
