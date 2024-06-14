## types
## can check the type using type function type()

a_string = "Cool String"
an_int = 12

print(type(a_string))
# prints "<class 'str'>"

print(type(an_int))
# prints "<class 'int'>"

print(type(5))  ##prints int

my_dict = {}
print(type(my_dict))  ##prints dict

my_list = []
print(type(my_list)) ##prints list 

##### Class

# A class is template for a data type 
# Define a class using a keyword 
# Use a capital 

## can define an empty class... 
class CoolClass:
  pass ##this provides a pass for the empty class 

### WE NEED TO CREATE AN INSTANCE OF THE CLASS rather than just defining it - THIS IS ALSO CALLED AN OBJECT

cool_instance = CoolClass() ## variable used to save the class

print(type(cool_instance))
# prints "<class '__main__.CoolClass'>" ## SHOWS COOL INSTANCE IS FROM CLASS COOLCLASS

class Facade:
    pass

facade_1 = Facade() ## same as above 
facade_1_type = type(facade_1)
print(facade_1_type) ## <class '__main__.Facade'>





