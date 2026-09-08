import random
import time
print("")
print("")
print("Welcome!")
print(" _______________________")
print("|Password Generator v1.0|")
print("|_______________________|")
x = input("Enter A Basic Password Which has to Be Transformed (Can Also Be left empty in order to generate a complete Password) : ")
y = random.randint(10000 , 9999999)
z = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","x","Y","Z"]
p = random.choice(z)
q = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
r = random.choice(q)
s = ["~","!","#","$","%","^","&","*","_","-","=","+",":",";","|"]
t = random.choice(s)
time.sleep(1)
print("")
print("Password Generated Successfully")
print("")
time.sleep(1.5)
print(f"Your Password is : {x}{y}{p}{r}{t}")
print("")
print("")
print("Thank You")