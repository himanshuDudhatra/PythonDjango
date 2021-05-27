# hash is use for single line comment
''' single inverted comma is use for multi line comment '''
"""double inverted comma is use for multi line comment """

#variables
v = 19
name = "himanshu"
print(name)
name = "dudhatra"
print(v)
print(name)
print('my name is ',name)

# check datatypes
print(type(v))
print(type(name))

#define value in other method
a,b,c = 1,8.1,"GEC,Modasa"

print(a,b,c)

a = b = c = 19

print(a,b,c)

#use of isintance() function

v = 19
v1 = 9.1
v2 = 9 + 3j
print(type(v2))

print(v,"is int", isinstance(19,int))
print(v2,"is complex", isinstance(9 + 3j,complex))
print(v2,"is complex", isinstance(9 + 3j,int))

#string

name = "My name is himanshu "
print(name)
print(name * 2)
#char print what ever you want
print("\nchar print what ever you want")
print(name[3])
print(name[1:6]) # which char you print
print(name[3:]) # what is your first char
print(name[:7])
print("contination use combine two string "+name)

#list
#use for store multiuple value
print("\n")
list = [1,3,4,"himasnhu",23.5,12]
print(type(list))
print(list)
print('list[1] = ',list[1])
print('list[1:3] = ',list[1:3])
print('list[2:] = ',list[2:])
print("\n")

#tuple
#tuple is same as list but once created cannot modified

tuple = (1,4,5,6,"himasnhu",1.2)
print(type(tuple))
print(tuple)
print("\n")

#dictionary
#dictionary are kind of hash data type
d = {1:'himanshu',2:'dudhatra',"string":10,3:19}
print(type(d))
print(d)
print("d[1] = ",d[1])
print("d[2] = ",d[2])
print("d[string] = ",d['string'])
