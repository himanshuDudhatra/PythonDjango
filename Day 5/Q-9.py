class Scheme:
    scheme_id = 1
    scheme_name = "VI india"
    outgoing_rate = "FREE"
    message_charge = 1.0
    def display(self):
        print("scheme_id: ",self.scheme_id)
        print("scheme_name: ",self.scheme_name)
        print("outgoing_rate: ",self.outgoing_rate)
        print("message_charge: ",self.message_charge)

class Customer(Scheme):
    cust_id = 1
    name = "Himanshu"
    mobile_no = 44544546
    def display1(self):
        print("cust_id: ",self.cust_id)
        print("name: ",self.name)
        print("mobile_no: ",self.mobile_no)

cust = Customer()
cust.display()
cust.display1()