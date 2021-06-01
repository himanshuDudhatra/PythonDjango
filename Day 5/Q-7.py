class cal6:
    n1 = ""
    n2 = ""
    area = ""

    def setData(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    
    def area(self):
        self.area = self.n1 * self.n2

    def display(self):
        print(self.area)

c1 = cal6()
i = int(input())
i1 = int(input())
c1.setData(i,i1)
c1.area()
c1.display()