class Publisher:
    name = ""

    def setValue(self,name):
        self.name = name

    def display(self):
        print("Name: ",self.name)

class Book(Publisher):
    pageNo=""

    def setValue1(self,no):
        self.pageNo = no

    def display1(self):
        print("pageNo: ",self.pageNo)

class Tape(Publisher):
    time = ""

    def setValue2(self,time):
        self.time = time

    def display2(self):
        print("Time: ",self.time)

b = Book()
t = Tape()
b.setValue("RENE ADLER")
b.setValue1(870)
t.setValue2(10)
b.display()
b.display1()
t.display2()