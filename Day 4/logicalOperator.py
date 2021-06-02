n1 = 50
n2 = 90
n3 = 7

# And Operator
if n1 > n2 and n1 > n3:
    print("N1 is largest ",n1)
if n2 > n1 and n2 > n3:
    print("N2 is largest ",n2)
if n3 > n1 and n3 > n2:
    print("N3 is largest ",n3)

# OR Operator
c = input('Input an alphabet:')

if(c=='a'or c=='A' or c=='e'or c=='E'or c=='i'or c=='I'or c=='o'or c=='O'or c=='u'or c=='U'):
    print("this cahr is vowels")
else:
     print('this char is consonants')