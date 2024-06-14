## each instance of a class can hold dofferent data types 
## data held by an object is called an instance variable 

class FakeDict:
    pass

fake_dict1 = FakeDict() ## instantiate object 1
fake_dict2 = FakeDict() ## instantiate object 2

fake_dict1.fake_key = "This works!"  ## assign instance variable 
fake_dict2.fake_key = "This too!" ## here too

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

#####

class Store:  ## class 
  pass

alternative_rocks = Store()  ## creates two objects from store class
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks" ##Gave both instance attributes of store name 
isabelles_ices.store_name = "Isabelle's Ices"


