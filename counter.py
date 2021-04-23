#1
print('Counter')
class counter:
    count=0
    def __init__(self):
        self.count=0
    def countUp(self):
        self.count+=1
c=counter()
c.countUp()
print(c.count)
c.countUp()
print(c.count)