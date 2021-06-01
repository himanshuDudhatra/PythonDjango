class employee:
    name = "Himanshu"
    designation = "Senior MERN Developer"

class emp(employee):
    salary = "210000"

    def info(self):
        print(self.name)
        print(self.designation)
        print(self.salary)

emp1 = emp()
emp1.info()