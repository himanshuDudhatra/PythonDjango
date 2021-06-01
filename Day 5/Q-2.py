class cal2:
    r=""
    
    def setDate(self,n1):
        self.r = n1
        print(self.__reduce__)
    
    def area(self):
        PI = 3.14
        area = PI * self.r * self.r
        return area
    
    def display(self,n):
        print("circle's area is ",n)

c1 = cal2()
n = float(input("enter the radius "))
c1.setDate(n)
n = c1.area()
c1.display(n)