# *args = parameter that packs all arguments into a tuple. it is useful so 
# that function can accept a varying amount of arguments

def add(*args): # args is a variable we can use *potato if we want
    sum = 0 
    for i in args:
        sum += i
    return sum # note: if you return inside the loop, loop only exceutes once

print(add(1,2,3,4,5,6,7))