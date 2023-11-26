# Question 1 
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print("Hello " + user_name)
    return None
hello_name("Kadeeja")


# Question 2 
# Write a python function, 
# first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    for number in range(1, 100, 2):
        print(number)
first_odds()
    

# Can we review how to solve questions 3-5? 


# Question 3 
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
  a_list = [1, 2, 3, 4, 5]
  max = 0
  print(max_num_in_list[1, 2, 3, 4, 5])
   

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
# The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    
# Question 5 
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    list = [1, 2, 3, 4, 5]
    for i in range(len(a_list))
