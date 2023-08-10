# Class or Static Variables in Python
# Features of Static Variables

# Static variables are allocated memory once when the object for the class is created for the 
# first time.

# Static variables are created outside of methods but inside a class

# Static variables can be accessed through a class but not directly with an instance.

# Static variables behavior doesn’t change for every object.


class Demo:
    
    # static_var
    name = "Joy"
    
    def __init__(self):
        self.FullName = 'Joy Sing'
        

if __name__ == "__main__":
    
    obj=  Demo() 
    print(obj.FullName) # Instance Variable
    print(Demo.name)
                
# Advantages:
# Memory efficiency: Since static variables are shared among all instances of a class, they can save memory by avoiding the need to create multiple copies of the same data.
# Shared state: Static variables can provide a way to maintain shared state across all instances of a class, allowing all instances to access and modify the same data.
# Easy to access: Static variables can be accessed using the class name itself, without needing an instance of the class. This can make it more convenient to access and modify the data stored in a static variable.
# Initialization: Static variables can be initialized when the class is defined, making it easy to ensure that the variable has a valid starting value.
# Readability: Static variables can improve the readability of the code, as they clearly indicate that the data stored in the variable is shared among all instances of the class.
# Disadvantages:
# Inflexibility: Static variables can be inflexible, as their values are shared across all instances of the class, making it difficult to have different values for different instances.
# Hidden dependencies: Static variables can create hidden dependencies between different parts of the code, making it difficult to understand and modify the code.
# Thread safety: Static variables can be problematic in a multithreaded environment, as they can introduce race conditions and synchronization issues if not properly synchronized.
# Namespace pollution: Static variables can add to the namespace of the class, potentially causing name conflicts and making it harder to maintain the code.
# Testing: Static variables can make it more difficult to write effective unit tests, as the state of the static variable may affect the behavior of the class and its methods.    