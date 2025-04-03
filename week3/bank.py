def credit(Amount,value):
    Amount +=value
    print(Amount)
    return Amount



def debit(Amount,value):
    Amount=Amount-value
    print(Amount)
    return Amount


def showbalance(Amount):
    print("balance amount in your account:",Amount)
    
    
    



Amount=0
Amount=credit(Amount,1000)
Amount=debit(Amount,200)
showbalance(Amount)
