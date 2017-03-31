booklist=[]
running=True
def addlist(blist):
	userinput=input("Enter the book name:")
	booklist.append(userinput)
def listbook(blist):
	if not booklist:
		print ("The list is empty")
	else:
		for i in booklist:
			print (i)
	print()
while(running==True):
	userinput=input("Type the command\n1.add\n2.list\n3.exit\n")
	if userinput=="1":
		addlist(booklist)	
	elif userinput=="2":
		listbook(booklist)	
	elif userinput=="3":
		running=False
	else:
		print ("Enter the valid commmand")
