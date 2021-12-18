from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.

class Food(models.Model):

    name = models.CharField(max_length=300, db_index=True)
    content = models.TextField()
    rasmi = models.TextField(max_length=300)
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name


class Aloqa(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    massage = models.TextField(default=0)
    number = models.IntegerField()
    address = models.CharField(max_length=300)

class Card(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="cards", on_delete=models.PROTECT, default=None)   
    is_sold = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}: {self.added_date}"

class CardItem(models.Model):
    food = models.ForeignKey(Food, related_name="carditems", on_delete=models.PROTECT, default=None)
    total = models.IntegerField(default=1)
    card = models.ForeignKey(Card, related_name="carditems",on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.food.name