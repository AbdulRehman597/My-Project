#this is a simple python file that demonstrates the use of function in python. A function is a block of code that performs a specific task. It can take input parameters and return a value. In this example, we have defined a function called 'cal' that takes two parameters 'a' and 'b' and returns their sum. We then call the function with different values to see the results.

def sum(a, b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print(sum(1, 2))
print(mul(3, 4))
print(div(6, 2))
print(div(5, 0))