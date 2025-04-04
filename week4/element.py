
def print_arr(li):
        for i in li:
              print(i,end=' ')



elements=[]
limit=int(input("enter limit for list: "))
for i in range(limit):
       val=int(input("enter value: "))
       elements.append(val)
       
print_arr(elements)
