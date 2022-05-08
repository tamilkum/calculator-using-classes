from audioop import mul
from re import sub


class Calculator():

    def __init__(self,num1,num2) -> None:
        self.num1=num1
        self.num2=num2


    def add(self):
        sum=self.num1+self.num2
        print("sum:",sum)
     
    def subract(self):
        sub=self.num1-self.num2
        print("sub:",sub)

    def multiply(self):
        mul=self.num1*self.num2
        print("mul:",mul)


c1=Calculator(5,2)
print(c1.add())
print(c1.subract())
print(c1.multiply())


        