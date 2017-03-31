class book(object):
    def __init__(self,name,author):
        self.name=name
        self.author=author
def addbook(booklist):
    name=input("Enter the book name:")
    author=input("Enter the author name:")
    booklist.append(book(name.upper(),author.title()))
def listbook(booklist):
    if not booklist:
        print("The list is empty")
    else:
        for i in booklist:
            print((i.name.upper(),i.author.title()))
def readbooks(booklist):
    blist=[]
    f=open(input("Enter the filename")) 
    for line in f:
        comma=line.find(",")
        name=line[0:comma]
        author=line[comma+1:]
        booklist.append(book(name.upper(),author.title()))
        print((name.upper(),author.title()))
    userinput=input("Do you want to save the read file into the temporary list?.\n Enter your option\n1.Yes\n2.No")
    if userinput=="1":
        for i in blist:
            booklist.append(i)
        print("Saved")
    else:
        print("Not saved")
    f.close()
def newfile(booklist):
    userinput=input("enter the file to create:")
    f=open(userinput,'w')
    for i in booklist:
        f.write("%s,%s"%(i.name.upper(),i.author.title()))
    f.close()                    
def existingfile(booklist):
    userinput=input("enter the file to create:")
    f=open(userinput,'a')
    for i in booklist:
        f.write("%s,%s"%(i.name.upper(),i.author.title()))
    f.close()
booklist=[]
running =True
while(running==True):
    userinput=input("\nEnter the option \n1.Add book to the temporary list\n2.list the books in the temporary list \n3.Read an existing file \n4.save new file\n5. Save existing file\n6.clear the temporary list\n7.exit\n")
    if userinput=="1":
        addbook(booklist)
    elif userinput=="2":
        listbook(booklist)
    elif userinput=="3":
        readbooks(booklist)
    elif userinput=="4":
        newfile(booklist)
    elif userinput=="5":
        existingfile(booklist)
    elif userinput=="6":
        booklist=[]
    elif userinput=="7":
        running=False
    else:
        print("Enter the valid command")

                    
