# These functions seem to be somewhat similar to S3 in R: 
# they are so called data-model methods: 
# https://docs.python.org/3/reference/datamodel.html

class Person(): 
    def __init__(self, name): 
        self.name = name 
    def __repr__(self):
        return f"My name is {self.name}"
        
        
person = Person("Peter")
print(person)
        
        
        