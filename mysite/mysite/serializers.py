# import serializers
from rest_framework import serializers
# import drink model so we can serialize it
from .models import Drink

# Create serialization class
class DrinkSerializer(serializers.ModelSerializer):

    # Create inner class for metadata of model
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
        
