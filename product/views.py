from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BaseAuthentication
from rest_framework import filters
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import api_view, schema
import json
from django.http import JsonResponse

@api_view(['GET'])
def get_menu(request):
    foods = Food.objects.all()
    datas = list(foods.values())
    for data in datas:
        category = Category.objects.get(id=data["category_id"])
        data["category_id"] = category.name
    return JsonResponse(datas, safe=False)

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filterset_field = ['name', 'content']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', 'price']
    ordering = ['name']
    search_fields = ['name']
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class FoodNumberPaginations(PageNumberPagination):
#     page_size = 3

class AloqaViewSet(viewsets.ModelViewSet):
    queryset = Aloqa.objects.all()
    serializer_class = AloqaSerializer
    filterset_field = ['name', 'number']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', 'number']
    ordering = ['name']
    search_fields = ['name']

class CardItemViewSet(viewsets.ModelViewSet):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer        
    permission_classes = [IsAuthenticated]

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]