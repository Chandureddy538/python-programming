bal=0
trans=[]
while true:
	print("welcome to bank app")
	print("press 1 for credit")
	print("press 2 for debit")
	print("press 3 for show balance")
`	print("press 4 for last 5 transactions")
	print("press 5 for for exit")
choice=int(input("enter the choice"))

def credit(amount,bal,trans):
	bal+=amount
	print(amount,"bal credit successfully")
	trans.append(amount)
	return bal,trans

def debit(amount,bal,trans):
	if bal<amount:
	       print("insufficent bal")
	       else:
	              bal-=amount
	              print(amount,"bal debit sucessfully")
                      trans.append(amount)
                      return bal,trans
                    
def show_bal(amount):
	    print("balance amount in u r account:",amount)

def last_five_transaction(trans):
	print("all transaction")



if (choice==1):
        amount=int(input("enter the amount"))
        bal,trans=credit(amount,bal,trans)
elif (choice==2):
	amount=int(input("enter the amount"))
        bal,trans=debit(amount,bal,trans)
elif (choice==3):
	showbalance(amount)
elif (choice==4):
	lastfive(trans)
else:
    exit
