from django.db              import models
from django.utils           import timezone
from django.core.exceptions import ValidationError

"""
Remember the three-step guide to making model changes:
1- Change your models (in models.py).
2- Run python manage.py makemigrations to create migrations for those changes
3- Run python manage.py migrate to apply those changes to the database.
***IMPORTANT: django comes with a builtin API, run:
1- python3 manage.py shell
2- p = Post(None, 'Jorgeley <jorgeley@gmail.com>', 'Is Django nice?', 
    'Well, it seems to me that Django is a good option for who wants to code 
    like a man in Python', timezone.now())
3- p.save()
4- p.id
5- Post.objects.all()
@see: https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models
"""

#class Comment inherits models.Model and has relationship with Post class
class Comment(models.Model):
    post    = models.ForeignKey('Post', on_delete=models.CASCADE) #relationship
    author  = models.CharField(max_length=200)
    comment = models.TextField()
    
#class Post inherits models.Model
class Post(models.Model):
    #these attributes will be mapped to database fields
    author      = models.CharField(max_length=200)
    title       = models.CharField(max_length=200)
    text        = models.TextField()
    publishing  = models.DateTimeField('date published')
    # this is another way of stablishing the relationship between Comment and Post
    #comments    = models.ManyToManyField(Comment, related_name='post_comments')
    
    """
    OVERRIDING THE CONSTRUCTOR
    turns out that overriding the constructor to raise an exception or to do any
    kind of validation is a bad idea if you have already something in your model 
    that is invalid, I tried and leaded to several exceptions in any other method 
    like 'order_by(), all()', etc because I had already saved before posts in 
    the future and the __init__ is called on every object instantiation of course
    """
    def __init__(self, id, author, title, text, publishing, *args, **kwargs):
        if publishing > timezone.now():
            """
            here's the thing: if you saved previously a 'publishing' date in the
            future, this exception will fire even for other methods like 
            'order_by(), all()', etc due to the __init__ method being called by
            them, just bear this in mind
            """
            raise ValidationError("You can't publish in the future")
        else:
            super().__init__(self, *args, **kwargs)  # Call the parent constructor
            self.pk         = id
            self.author     = author
            self.title      = title
            self.text       = text
            self.publishing = publishing
    
    def getComments(self):
        return Comment.objects.all().filter(post_id=self.id)
    
    #this would be another way of doing the validation already done in the constructor
    """
    def __setattr__(self, name, value):
        if name == 'publishing':
            if value > timezone.now():
                raise ValidationError("You can't publish in the future")
        super(Post, self).__setattr__(name, value)
    """