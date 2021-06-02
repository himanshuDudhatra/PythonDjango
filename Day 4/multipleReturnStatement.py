from functionWithReturnStatement import hello


def hello():
    name = 'Dudhatra Himanshu'
    location = 'Modasa'
    college = 'Government Engineering College'
    return name,location,college

name,location,college = hello()
print('Name:',name)
print('Location:',location)
print('College:',college)
