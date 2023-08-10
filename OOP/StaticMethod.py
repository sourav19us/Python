# Static method in Python


class  Demo:
    FullName ="Hi"
    def __init__(self):
        self.Name = "Joy"
        
    @staticmethod # static method  is not use a class var
    def show():
        print(f" name is ")    
        

if __name__ == "__main__":
    obj = Demo() 
    Demo.show()       