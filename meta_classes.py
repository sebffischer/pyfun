# How does Python create objects? 

class Person(): 
    def __init__(self):
        pass
        
        
person = Person() 

# is actually the same as: 

Person = type("Person", (), {})

person = Person() 

# so the class Person() ... is just a syntax specification for a function call
# i.e. the function type is called 