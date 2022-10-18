from django.contrib import admin

from main_app.models import Category
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Book)