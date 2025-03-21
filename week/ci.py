p=int(input("enter the prinicipal:"))
r=float(input("enter the rate:"))
t=int(input("enter the time:"))
A=p*(((1+r/100)**t))
ci=A-p
print("compound interest:",ci)
