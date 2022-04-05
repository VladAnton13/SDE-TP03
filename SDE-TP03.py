
var1=12
x=type(var1)
print (x)

var2 = 17.9
y=type(var2)
print (y)

var3 = "SdE"
z=type(var3)
print (z)

num=29
flag= False
if num > 1:
    for i in range(2, num):
        if (num % i)== 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

data = ['Apple', 'Melon', 'Orange', 'Lemon', 'Peach']
print("The sorted elements are")
print(sorted(data, reverse=False))

data = ['Apple', 'Melon', 'Orange', 'Lemon', 'Peach', 'Black','White','Red']
print("The inverted elements are")
print(sorted(data, reverse=True))