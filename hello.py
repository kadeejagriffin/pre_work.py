# Create a function that takes a name as an argument and 
# returns a new string that says Hello and then the name
# that was the argument
# Then use this fucntion and ask the use for their namme
# and tell them hello

print("John")

name = "John"
print(name)

print("Hello", name)
print("Hello " + name)
hello_john = "Hello" + " " + name
print(hello_john)

print("Our function is defined below")
def say_hello_print(the_users_name):
    print("Hello" + the_users_name )
    return None

print("Using our fuction with the print statement inside")
say_hello_print("John")
print(say_hello_print("John"))

def say_hello_return(the_users_name):
    return "Hello " + the_users_name

print("using our function with the return statment inside and not printing")
print(say_hello_return("Steve") == "Hello Steve")


print (say_hello_return(" Steve"))
hello_steve = say_hello_return("Steve")
print(hello_steve)


users_name = input("What is your name? ")
#print(users_name)
#print(type(users_name))
print(say_hello_return(users_name))