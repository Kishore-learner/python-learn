class Car:
    wheels = 4 #class variables : common to all object
    
    def __init__(self,make,model,color,year):
        self.make = make #instance variable : may or may not be same for all other objects
        self.color = color #instance variable
        self.model=model #instance variable
        self.year= year #instance variable
    
    def Drive(self):
        print("you've driven the",self.make,self.model)
    
