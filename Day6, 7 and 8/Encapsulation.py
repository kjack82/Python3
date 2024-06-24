# This is the idea of wrapping data and methods that work on data within one unit. 
# This restricts accessing variables and methods directly and can help ensure accidential modifation does not occur. 

# A class is an example of excapsulation - keeping all the data of members functions and variables. 

# Keeps data hidden from other sections. 

# Python program to 
# demonstrate protected members 
  
# Creating a base class 
class Base: 
    def __init__(self): 
  
        # Protected member 
        self._a = 2
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
  
        # Calling constructor of 
        # Base class 
        Base.__init__(self) 
        print("Calling protected member of base class: ",  
              self._a) 
  
        # Modify the protected variable: 
        self._a = 3
        print("Calling modified protected member outside class: ", 
              self._a) 
  
  
obj1 = Derived() 
  
obj2 = Base() 
  
# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected member of obj1: ", obj1._a) 
  
# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2._a) 

# Calling protected member of base class:  2
# Calling modified protected member outside class:  3
# Accessing protected member of obj1:  3
# Accessing protected member of obj2:  2