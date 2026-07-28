# Arithmetic Operators
a = 10
b = 20
print(a+b) #  + this is addition Operators

c = 10
d = 20
print(c-d) # - this is substraction

e = 20
f = 30
print(e*f) # * this is multiplication

x = 100
y = 25
print(x/y) # / this is Division

x1 = 100
y1 = 30
print(x1%y1) # % this is modulor 

i = 40
o = 17
print(i//o) # // this is floor division


a1 = 10
a2 = 3
print(a1**a2) # ** this is  Exponentiation (power) operator

# Assignment Operator
m = 3
m += 10 #  x = x+10
print(m)

m -= 1 # x = x - 1
print(m)

m *- 2
print(m)

m /= 3
print(m)

m %= 4
print(m)

m **= 200
print(m)


# comparison Operators.
z = 100
#print(z <= 11,"This is eligible for Driving")
if z < 180:
    print("Eligible for Driving")
else:
    print("Not Allowed ")

#==
if z == 100:
    print("Qualify")
else:
    print("not Qualify")
counts = ""
for counts in range(10):
    print("Counting :",counts)

name = int(input("Inter a number:"))
if name >= 70:
    print("you are passed in A grade")
elif name >= 40:
    print("you are passed in B Grade")
elif name >= 33:
    print("you are passed in C Grade")
else :
    print("Sorry you are Failed in this Year")

# != 
a_1 = 100
a_2 = 10
c_1 = a_1 != a_2
print(c_1)

num = 100
num_1 = 100
print(num > num_1) # > grater then operator
print(num < num_1) # less then operator
print(num >= num_1) #grator then equal to
print(num <= num_1) # less then equal to 

#logical operator

User_name = str(input("Enter Your User Name:"))
password = str(input("Enter Your Password:"))
if User_name == 'Suryanshu' and password == 'Suryanshu12@':
    print("Welcome", User_name)
else:
    print("Not Exists")

ham = 100
ham_1 = 1000
print(ham >10)
print(ham_1<200)

# Precedence operators.
print(5+10*10-10)
print(2**10)
print(5+2*3**2)
print(5**2**3)
print(5*5*3)