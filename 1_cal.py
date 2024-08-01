n = int(input("enter 1st digit : "))
m = int(input("enter 2nd digit : "))
s = str(input("enter the function [+,x,%,/,^,//] : "))
ans = int
if s == "+":
    ans = n+m
elif s=="x":
    ans = n*m
elif s=="%":
    ans = n%m
elif s=="/":
    ans = n/m
elif s=="//":
    ans = n//m
elif s=="^":
    ans = n**m
else:
    print("invalid")
print(ans)


'''
this project is simple one.. I know!! this is did in order to recall how to use version control using git 
'''
