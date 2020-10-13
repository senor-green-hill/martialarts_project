from django.contrib import admin
from .models import Requirement, Category, Rank, Media

# Register your models here.
admin.site.register(Requirement)
admin.site.register(Category)
admin.site.register(Rank)
admin.site.register(Media)