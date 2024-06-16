


class Calculator :
    
    def addition(self,a,b):
        return a+b 
    
    def subtraction(self,a,b):
        return a-b 
    
    def multiplication(self,a,b):
        return a/b
     
    def division(self,a,b):
        if b==0:
            raise Exception("Some error")
        return (a//b)

obj_Calculator = Calculator()
div=obj_Calculator.division(9,2)
print(div)