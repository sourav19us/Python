#  Printing Objects 

# Printing objects give us information about objects we are working with. In C++, we can do 
# this by adding a friend ostream& operator << (ostream&, const Foobar&) method for the class. 
# In Java, we use toString() method.
# In python, this can be achieved by using __repr__ or __str__ methods.


class Test:
    
    def __init__(self,Name):
        self.Name = Name
        
    def __str__(self):
        return f"Name from __str__ is {self.Name}"  
          
    def __repr__(self):
        return f"Name from __str__ is {self.Name}"
    
    
# f no __str__ method is defined, print t (or print str(t)) uses __repr__
class Test1:
    
    def __init__(self,Name):            
        self.Name = Name
    
          
    def __repr__(self):
        return f"Name from __str__ is {self.Name}"


if __name__ == '__main__':
      
      obj = Test("Joy")
      print(obj)      
      print([obj])    
      
      ob1 = Test1("Joy")  # in Test1 only __repr__ function
      print(ob1)
      print([ob1])
      

      
      
       