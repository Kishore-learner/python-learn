def hello():
    x = "hello world"
    global y
    y = "hello world again"
    print(x)

hello()
# print(x)
print(y)

# LEGB -> local, enclosed, global, builtin variables 
# a function checks variables in this order