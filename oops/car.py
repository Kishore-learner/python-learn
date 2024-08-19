class Car:

    def __init__(self,make,model,color,year):
        self.make = make
        self.color = color
        self.model=model
        self.year= year
    
    def Drive(self):
        print("you've driven the",self.make,self.model)
    
