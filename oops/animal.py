class Animal:

    alive = True

    def __init__(this,name,color):
        this.name = name
        this.color = color
    
    def sound(this):
        if this.alive == True:
            print(this.name,"makes sound")
        else:
            print("sh*ts dead!")