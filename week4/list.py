def creat_list(l,n):
	for i in range(n):
	        temp=int(input())
	        l.append(temp)
	return l
l1=[]
l2=[]
l3=[]
n1=int(input("enter the numbers:"))
n2=int(input("enter the numbers:"))
n3=int(input("enter the numbers:"))
print("enter numbers in first list")
l1=creat_list(l1,n1)
print(l1)
print("enter numbers in second list")
l2=creat_list(l2,n2)
print(l2)
print("enter numbers in the third list")
l3=creat_list(l3,n3)
print(l3)                                                       
	
