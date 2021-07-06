class Person:
    def __init__(self,initialAge):
        self.initalAge=age
        if(self.initalAge<0):
            print("Age is not valid, setting age to 0.")
            self.initalAge=0
    def amIOld(self):
        if(self.initalAge<13):
            print("You are young.")
        elif(self.initalAge>13 or self.initalAge<=20):
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.initalAge=self.initalAge+1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
