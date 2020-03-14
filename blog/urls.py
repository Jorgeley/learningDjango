"""
this is the route file for the "blog" app
route files are basically maps of URLs to views

Route:
Patterns don’t search GET and POST parameters, or the domain name. Examples:
https://www.example.com/myapp/, the URLconf will look for myapp/
https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/

View:
When Django finds a matching pattern, it calls the specified view function with 
an HttpRequest object as the first argument and any “captured” values from the route 
as keyword arguments. So, 'views.index' maps to file views.py function index(request)
"""
from django.urls import path
from . import views

app_name = 'blog' #sets namespace

urlpatterns = [
    #    route                      view            name of the route
    path('',                        views.index,    name='index'),
    # /blog/5/
    path('<int:post_id>/',          views.detail,   name='detail'),
    # /blog/5/comments/
    path('<int:post_id>/comments/', views.comments, name='comments'),
    # /blog/5/comment/
    path('<int:post_id>/comment/',  views.comment,  name='comment'),
]