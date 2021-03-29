#Progrm to check the validity of a password by the following criteria:-
# must have more than 6 and less tnan 12 characters
# must have one capital and one small letter
# must have at least one symbol from #$@

import re      
#imports regular expression library
passwords = input("Enter the passwords you would like to have: ").split(",")  
# takes input from the user and store in passwords
# split function split more than one passwords by comma seprated form
validPasswordFound = False   
# take booean variable and suppose it is false
for password in passwords:   
    # tqke password one by one from passwords
    if(len(password) >= 6 and len(password) <= 12) and re.match(r'.*[A-Z] .*' and r'.*[a-z].*' and r'.*[0-9].*' and r'.*[#$@*\/].*' , password):
        # this is for checking  the above condition of given criteria
        print(password) 
        # when the above condition true then it will print the pssword
        validPasswordFound = True 
if(not validPasswordFound):
    print("INVALID PASSWORD")  
    # else it will print the invalid password

# we can also used as by using ladder if or by above method by using only one if condition.
#if re.match(r'.*[A-Z] .*' and r'.*[a-z].*' and r'.*[0-9].*' and r'.*[#$@*\/].*' , password):
            #if re.match(r'.*[a-z].*', password):
                #if re.match(r'.*[0-9].*', password):
                    #if re.match(r'.*[#$@*\/].*', password):

# regular expression is a library which searches the charcater digit symbols .
# we can use regx 101 for showing the result of any regular expression that wgat it actual does.