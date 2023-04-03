from django.contrib import admin
from .models import *
# Register your models here.
class PostRegistration(admin.ModelAdmin):
    list_display=['id','title','desc']

admin.site.register(Post,PostRegistration)