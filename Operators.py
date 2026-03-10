# Arithmetic Operators
a = 10
b = 5
c = a+b #add
print(c)
d = a-b  #sub
print(d)
e = a*b  #mul
print(e)
f = a/b  #div
print(f)  
g = a//b  #floor div
print(g)
h = a%b  #modulo
print(h)
i = a**b  #exponent
print(i)

# Assignment Operators

num = 10   # assignment

a += b  # add and assign
print (a)
a -= b   # subtract and assign
print(a)
a *= b  # multiply and assign
print(a)
a /= b   # divide and assign
print(a)
a //= b  # floor divide and aasign
print(a)
a %= b  # modulo and assign
print(a)
a **= b  # expo and assign
print(a)

# Comparision Operators

print(a == b)  # equal to
print( a != b)  # not equal to
print(a > b)  # grater tham
print(a < b)  # less than
print(a >= b)  # grater or equal
print(a <= b)  # less or equal

# Logical Operators

x = True
y = False
print( x and y)
print(x or y)
print( not x)

# Membership Operators
L =[1,2,3,4,5]
print(1 in L)
print(10 not in L)

# Identity Operators
name_1 = "john"
name_2 = "john"
result1 = name_1 is name_2
print(result1)

num_1 = 10
num_2 = 20
result2 = num_1 is not  num_2
print(result2)

# Bitwise operators
n = 2
m = 3
print(n&m)  # bitwise AND 
print(n|m)  # bitwise OR
print(n^m)  # bitwise XOR
print(~n)   # bitwise NOT
print(2>>1)  # right shift
print(2<<1)  # left shift