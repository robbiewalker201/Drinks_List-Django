# Import admin functionality
from django.contrib import admin
# Import model we just made that we want to admin control
from .models import Drink

# Pass the model we made to the Django Admin site
admin.site.register(Drink)

'''
We have now added the model 'Drinks' to the Django admin page which is where the information
in the model 'Drinks' will be stored. This gives us a way to add data to the database that stores 
the information for this website
'''
