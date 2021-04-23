#2
from OOP.counter import counter
class countdown(counter):
    def __init__(self):
        super().__init__()
    def countdown(self):
        self.count-=1


c1=countdown()
c1.countUp()
c1.countUp()
c1.countdown()
print(c1.count)




