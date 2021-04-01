# Program to print prime numbers between the given intervals

lower_bound = int(input("Enter the lower_bound  number :")) # lower bound will be the number from where we want to start our prime number printing
upper_bound = int(input("Enter the upper_bound number :")) # upper bound will be the number till that we want to stop our prime number printing
if lower_bound > 1 : 
    for  i in range (lower_bound , upper_bound + 1):  # it takes one nuber at a time in variable i then check one by one 
            for j in range(2,i): # here the loop will run till the variable i 
                if (i%j)==0:  # condition check here if i modulas j == 0 then it will break the loop 
                    break
            else :
                print(i)   # else print the value of i 
else:
    print("Enter invalid input") # else it will print this if upper both conditions not satisfied

'''
OUTPUT:-
Enter the lower_bound  number :100
Enter the upper_bound number :200
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
'''