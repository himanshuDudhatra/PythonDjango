class Publisher:
    name = "RENE ADLER"
    def display(self):
        print("Name: ",self.name)

class Book(Publisher):
    pageNo = "870"
    def display1(self):
        print("pageNo: ",self.pageNo)

class Tape(Publisher):
    time = 10
    def display2(self):
        print("Time: ",self.time)

b = Book()
t = Tape()
b.display()
b.display1()
t.display2()