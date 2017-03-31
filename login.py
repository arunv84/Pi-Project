username="Arun"
password="aishu"
userinput=raw_input("What is your username?")
if userinput == username:
    
    userinput=raw_input("Password?")
    if userinput==password:
        print "Welcome"
    else:
        print "wrong password"
elif userinput == "dhesna" or userinput ==" Dheshna":
        print "not allowed"
else:
        print"wrong username"
