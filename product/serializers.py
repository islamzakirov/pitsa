from django.db.models import fields
from rest_framework import serializers
from .models import *

class CardItemSerializer(serializers.ModelSerializer):    

    class Meta():
        model = CardItem
        fields = '__all__'
 
class CardSerializer(serializers.ModelSerializer):    
    carditems = CardItemSerializer(read_only=True, many=True)
    class Meta():
        model = Card
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta():
        model = Food
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'

class AloqaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Aloqa
        fields = '__all__'