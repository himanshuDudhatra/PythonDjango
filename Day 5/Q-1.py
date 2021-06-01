class cal1:
    n1=0
    n1=0
    n3=0

    def setData(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def display(self):
        n = self.n1 + self.n2 + self.n3
        print(n)

c1 = cal1()
n = int(input())
c1.setData(n,2,3)
c1.display()