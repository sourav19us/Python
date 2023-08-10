# Data hiding 

# In Python, we use double underscore (Or __) before the attributes name and those attributes
# will not be directly visible outside. 

class Demo:
    __Name = ''
    
    def __init__(self,Name) -> None:
        try:
            self.__Name = Name 
        except Exception as e:
            print("Error is ",e)    
    
    def __del__(self): # Destructors when Object is deleted
        print(f"Object is deleted and Name is {self.__Name}")
        
if __name__ =="__main__":
    obj = Demo("joy")     
    
    try:
        print(obj.__Name) #Error is  'Demo' object has no attribute '__Name'
    except Exception as e:
        print("Error is ",e)    