from django.contrib import admin

# Register your models here.
from .models import *

class HomepageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rasmi')
    list_display_links = ('name',)
    search_fields = ('name', 'rasmi')
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food)