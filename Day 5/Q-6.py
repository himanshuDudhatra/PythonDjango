class cal5:
    r1=""
    r2=""
    a=""

    def __init__(self,r1,r2):
        self.r1 = r1
        self.r2 = r2
    
    def calArea(self):
        self.a = self.r1 * self.r2
    
    def display(self):
        print("area of rec is ",self.a)
    
c = cal5(3,2)
c.calArea()
c.display()