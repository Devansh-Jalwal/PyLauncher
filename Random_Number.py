import random
import time
print("Here You Go!")
time.sleep(0.5)
while True:
 x = int(input("From (Should Not be a Decimal) : "))
 y = int(input("To (Should Not be a Decimal) : "))
 z = random.randint(x,y)
 print(z)
 xyz = input("Want more? press 'y' for yes and 'n' for no : ")
 if xyz == "n":
  quit()
 else:
  print("")
  time.sleep(1.5)