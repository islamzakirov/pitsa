from django.db import models

class Gallery(models.Model):
    image = models.ImageField(default=True)
# Create your models here.

    def __str__(self) -> str:
        return self.image