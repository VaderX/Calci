#This application will do basic and advanced calculations

print ("Enter the value of A and B\n")

a, b = map(int, input().split(" "))

print("Select the following options\n")
print("1. Addition\t 2.Subtraction\n3.Multiplication\t 4.Division\n5.Modulous (Extra Feature)")
value = input()

if(value == '1'):
    print("Addition of A and B is: %d"%(a+b))
elif(value == '2'):
    print("Subtraction of A and B is: %d" %(a-b))
elif(value == '3'):
    print("Multiplication of A and B is: %d"%(a*b))
elif(value == '4'):
    print("Division of A and B is: %f"%float((a/b)))
elif(value == '5'):
    print("Modulous of A and B is: %d"%(a%b))
else:
    print("You've entered the wrong value, check your value first")
