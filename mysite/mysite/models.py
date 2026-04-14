# Import the models class from Django
from django.db import models

# Create a class for Drink with relevant attributes
# create is of the models tool 'Model'
class Drink(models.Model):
    # Each drink will have a name
    name = models.CharField(max_length=200)
    # Each drink will have a description
    description = models.CharField(max_length=500)

    # We can add __str__()
    # This is a special method (dunder) that states 
    # how an object of that class is converted into
    # a human readable string - "What should the object look like when printed?"
    def __str__(self):
        return "Name: " + self.name + " | Description: " + self.description

    '''
    for example, without this function print(object) = "<__main__.User object at 0x__________>"

    but with this function, if you create an object and print it you get print(object) = whatever __str__ returns
    '''

