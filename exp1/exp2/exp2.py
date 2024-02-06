#Conditional Statement
num = int(input("Enter the number\n"))
if num>5:
    print(num," is greater than 5")
    if num >=10 and num<= 20:
        print(num,"is in range from 10 to 20")
    else:
        print("Out of range of 10 to 20 ")    
elif num<5:
    print(num ,"is not greater than 5")
    if num >= -10 and num<= 0:
       print(num,"is in range of 0 to -10")
    else:
        ("the number is out of range")   
       
else:
    print("The entered number is 5 ")
    print("It is range of 1 to 10 ")
    
#loops
num = int(input("Enter the number\n"))
s= input("Enter a string\n")
i=0
while i<num:
        print(i)
        i+=1

for x in s:
    print(x)