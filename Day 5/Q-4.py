class cal4:
    n = ""

    def setData(self,n):
        self.n = n
    
    def sum(self):
        return self.n * self.n

    def display(self,n1):
        print(n1)

c1 = cal4()
c1.setData(2)
n = c1.sum()
c1.display(n)