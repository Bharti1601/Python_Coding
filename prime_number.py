# Program to check prime number

#x = int(input("Enter the number :"))
num = 409
flag =0
if num>1:
    for i in range(2, num//2 +1): 
        if num % i == 0:
            print("{} is not a prime number".format(num)) # if satisfies the if condition then it will print not a prime number
            flag = 1
            break
    if flag == 0:
        print("{} is  a prime number".format(num)) # if not satisfies the upper if condition and the flag = 0 then it will print prime number
        

'''
This will be the output:-
409 is  a prime number
'''        
