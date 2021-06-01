class cal3:
    P = ""
    R = ""
    N = ""
    I = ""

    def __init__(self,P,R,N):
        self.P = P
        self.R = R
        self.N = N

    def calInterest(self):
        self.I = float((self.P * self.R * self.N)/100)
    
    def display(self):
        print(self.I)

c1 = cal3(100,12,10)
c1.calInterest()
c1.display()