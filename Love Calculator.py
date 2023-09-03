# 🚨 Don't change the code below 👇
print("Welcome to the Compatible Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Makes all letters lowercase 
combined_names = name1 + name2
lower_case = combined_names.lower()

#Counts for the word true 
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true = t + r + u + e

#Counts for the word love 
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e

true_love = int(str(true) + str(love)) 

if (true_love >=40) and (true_love <= 50):
  print(f"Your love score is {true_love},You are alright together")
elif (true_love >=90) or (true_love<=10):
  print(f"Your love score is {true_love}, You go together like coke and mentos.")
else:
  print(f"Your love score is {true_love}, You might not work too well =(")
