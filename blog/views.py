"""
Honestly, this doesn't look to me like a view but a Controller, considering the 
MVC design pattern, but Django uses MTV whereas T stands for Template and V(View) 
does the logic between Models and Templates, like a controller basically, as said 
before, this is MTV.
Remember: these functions are mapped according to the routes defined in the blog/urls.py
"""
from django.shortcuts   import render
from django.http        import HttpResponse, Http404, HttpResponseRedirect
from django.urls        import reverse
from .models            import Post, Comment

def index(request):
    """    
    retrieve the last Post objects ordered by publishing
    you could also do: Post.objects.order_by('publishing')[:10]
        ...to retrieve only the last 10 posts
    """
    latest_posts = Post.objects.order_by('publishing')
    context = { #parameters to be passed to the template
        'latest_posts': latest_posts,
    }
    #render the template within the parameters above
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    try:
        #there's a shortcut for this: post = get_object_or_404(Post, pk=post_id)
        #but I prefer the following since is more object oriented style
        post = Post.objects.get(pk=post_id) #gets a post object by id
        comments = post.getComments()
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return render(request, 'blog/detail.html', {'post':post, 'comments':comments})

def comment(request, post_id):
    try:
        post = Post.objects.get(pk=post_id) #gets a post object by id
        comment = Comment( #creates a new Comment model object
            None, 
            post_id, #this can fire a KeyError exception if post_id not valid
            request.POST['author'], 
            request.POST['comment'])
        comment.save()
    except (KeyError, Post.DoesNotExist):
        raise Http404('Post does not exist')
    #it's always a good practice doing a redirection after posted data
    return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))

def comments(request, post_id):
    return HttpResponse(f"Comments for post {post_id}:")