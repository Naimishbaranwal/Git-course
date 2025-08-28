import numpy

class Students:

    def __init__(self,name:str,marks:int):
        self.name=name
        self.marks=marks

    def pass_fail(self):
        if self.marks<30:
            return "student has failed"
        else:
            return "student has passed"
        
    def call_parents(self):
        if self.pass_fail()=="student has failed":
            return "call his parents"
        else:
            return "don't call his parents"
        

a=Students('naimish',36)
a.call_parents()