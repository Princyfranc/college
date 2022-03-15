t=0.20
sd=10000
d=3000
i=float(input("Enter the gross income:"))
no=int(input("Enter the number of dependants:"))
ti=i-sd-(d*no)
tax=ti*t
print("The income tax is $"+str(tax))
