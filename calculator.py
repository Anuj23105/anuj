print("claculator")
print("1.add 2.subtraction 3.multiplication 4.division")
b=int(input("chose the no. for calculation"))
num1=int(input("enter first number"))
num2=int(input("enter second number"))
if b==1:
    print("sum of the no. is",num1+num2)
elif b==2:
    print("subtraction of no. is",num1-num2)
elif b==3:
    print("multiplication of this no. is",num1*num2)
elif b==4:
    print("division of this no. is",num1/num2)
else:
    print("wrong input")
print("thankyou")
