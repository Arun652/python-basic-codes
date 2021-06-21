class Person:
    def __init__(self,initialAge):
        self.initalAge=age
        if(self.initalAge<0):
            print("Age is not valid, setting age to 0.")
            self.initalAge=0
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if(self.initalAge<13):
            print("You are young.")
        elif(self.initalAge>13 or self.initalAge<=20):
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
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
