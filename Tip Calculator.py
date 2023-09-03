#Tip Calculator

Bill = int(input("how much was the bill? $"))
Tip = float(input("What is the percentage of tip? 10, 12, 15? "))


Tip1 = float((Tip*Bill))/100 + Bill
People = int(input("How many people will be splitting the bill? "))
Split = Tip1/People
Final = round(Split,2)
Final = "{:.2f}".format(Final)
print(f"Each person should pay ${Final}")