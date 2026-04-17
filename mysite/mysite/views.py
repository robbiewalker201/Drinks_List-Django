'''
This is where we create all of our endpoints
'''

# Import Json module
from django.http import JsonResponse
# Import Drink model
from .models import Drink
# Import serialization inner class
from .serializers import DrinkSerializer
# Import api_views
from rest_framework.decorators import api_view

# Response is a Django rest framework tool for allowing parsing of JSON data so that we can
# use the data in the Django HTML format on a web page
from rest_framework.response import Response
from rest_framework import status

# We are going to use a decorator to declare the API methods we could use
# This decorator is a Django rest api decorator, it controls what HTTP methods are allowed
@api_view(['GET', 'POST'])
# This function is an API endpoint
# 'request' is a DRF Request object
def drink_list(request):

    # Handles getting an existing drink
    if request.method == 'GET':
        # Get all drinks from sql database using Djangos ORM 
        # ".all()" = "SELECT * FROM drink;"
        drinks = Drink.objects.all()
        # Serialize them, many = True means serialize all
        # Serializers are needed to convert python objects 'drinks = many objects' into JSON data
        serializer = DrinkSerializer(drinks, many=True)
        # return JSON - sets content type to application/json
        # Django only allows dictionaries, since this is a list, SAFE must be false
        return JsonResponse(serializer.data, safe=False)
    
    # Handles creating a new drink
    # Content-type application/json - POST /drinks/
    if request.method == 'POST':
        # Create a seralizer for the input data so it is format ready
        serializer = DrinkSerializer(data=request.data)
        # If the content inputted matches the rules defined by the class DrinkSerializer
        if serializer.is_valid():
            # Saev the new Drink model instance to the database
            serializer.save()
            # Return Response NOT JsonResponse - tells that valid data created using correct POST notation (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# We are now craeting a new view which will be a new webpage 
# HTTP address for specific information about the drinks
@api_view(['GET', 'PUT', 'DELETE'])
# Need to pass id as argument for drink we want data for
def drink_detail(request, id):

    try:
        # Get an object Drink (row in database) based on primary key id
        drink = Drink.objects.get(pk=id)
    # if the id arguement passed does not exist, do this
    except Drink.DoesNotExist:
        # return HTTP error for data that does not exist in database
        return Response(status=status.HTTP_404_NOT_FOUND)

    # If GET request (get data from database)
    if request.method == 'GET':
        # Serialize the object retrieved from database using .get()
        serializer = DrinkSerializer(drink)
        # Return JSON formatted data, HTTP 200 for successful GET request
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        pass


    elif request.method == 'DELETE':
        pass