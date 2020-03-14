"""
this is the django builtin Admin Area
"""
from django.contrib import admin
from .models        import Post, Comment

admin.site.register(Post) #tells Django that Post model should be visible in the admin area
admin.site.register(Comment)