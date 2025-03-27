import random
n=random.rand(1,100)
print("guess the number:")
while True:
       x=int(input("random number"))
       if(x<n):
          print("too low")
       elif(x>n):
           print("too high")
        else:
           print("equal")
           break
