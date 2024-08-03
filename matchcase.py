x=int(input("enter : "))
match x:
    case 1:
        print("hey1")
    case 2:
        print("hey2")
    case 3:
        print("hey3")
    case 4:
        print("hey4")
    case _ if x<5: #new
        print("x lt 5")
    case _ if x>5: #new
        print("x gt 5")

# 
# we don't have to use break like c / c++. unlike c / c++ python matches the case and runs accordingly whereas
# c or c++ unless we add break, it will execute the next cases after the required cases.
# but catch is that once one case is executed other cases won't execute.
# 