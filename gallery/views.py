from django.shortcuts import render
from gallery.models import *
from .serializers import *
from rest_framework import viewsets

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer