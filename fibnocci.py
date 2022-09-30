#Function for nth fibnocci number using loop
def fibnocci(n):
    a=0
    b=1
   
    if n<0:
            print("Invalid input")
    elif n==1:
            print(b)
    else:
            for i in range(2,n+1):
                c=a+b
            
                a=b
                b=c
            print(c)
#Driver code
print(fibnocci(9))

