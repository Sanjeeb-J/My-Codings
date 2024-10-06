def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"
"""
greet is returning some value, but we are not capturing or use it in our program.
In order to capture and use it later on we have to store the return value inside a variable
It helps you to many things
"""
greeting = greet("hello, computer")
asking = greet("how is the weather?")
print(greeting)
print(asking)
