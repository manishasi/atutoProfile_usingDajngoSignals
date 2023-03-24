from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id","image","father_name","mother_name","dob","city","place","user")

admin.site.register(Profile,ProfileAdmin)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ["views","image","title"]

