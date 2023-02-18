# equation of a line:
# y = mx + b

"""
Key concepts:

variable
function
defining a function
declaring a variable
instantiating a variable

stretch:
module - a file that contains python code
"""

def get_y_value_of_a_straight_line(m,x,b):
    # equation of a line:
    # y = mx + b
    # given some slope m, and an intercept b, for any value of x we have a fixed value of y as the output
    y = (m * x) + b
    return y

print(get_y_value_of_a_straight_line(2,3,1))

# # declaration
# # int x; -> find me 8bits worth of space in memory to store a value we can call x - but i'm not sure what that value is yet.
# # print x -> null

# # instantiation
# # x = 3; -> remember that 8bit area of memory we found earlier? well now we're going to store the value 3 in that space.
# # print x -> 3

# # int x = 3;
# x = 3

def add_two_numbers(a,b):
    return a + b