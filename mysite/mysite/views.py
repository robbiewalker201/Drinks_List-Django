'''
This is where we create all of our endpoints
'''

# Import Json module
from django.http import JsonResponse
# Import Drink model
from .models import Drink
# Import serialization inner class
from .serializers import DrinkSerializer

# Function to get list of drinks
def drink_list(request):

    # Get all drinks
    drinks = Drink.objects.all()

    # Serialize them, many = True means serialize all
    serializer = DrinkSerializer(drinks, many=True)

    # return JSON
    return JsonResponse(serializer.data, safe=False)

