class TheFather:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

    def showMyself(self):
        print("TheFather's age = {0}".format(self.age))
       
    
class TheSon(TheFather):
     def showMyself(self):
        print("TheSon's age = {0}".format(self.age))