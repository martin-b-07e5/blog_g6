from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Post

from django.http import HttpResponse


# Create your views here.


# First view
# retrieve all the posts with the published status
#  using the published manager that you created previously.
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


""" 💡 You just created your first Django view.
    💡 The post_list view takes the request object as the only parameter.
        This parameter is required by all views.

    👀👀💡 In this view, you retrieve all the posts with the published status using the published manager that you created previously.

    👀👀💡 Finally, you use the render() shortcut provided by Django to render the list of posts with the given template.
    This function takes the request object, the template path, and the context variables to render the given template.

    It returns an HttpResponse object with the rendered text (normally HTML code). 

    The render() shortcut takes the request context into account, so any variable set by the template context processors is accessible by the given template.

    Template context processors are just callables that set variables into the context.
"""


# second view to display a single post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


""" 💡 This is the post detail view.
    👀 This view takes the year, month, day, and post arguments to retrieve a published post with the given slug and date.

    👀 Note that when you created the Post model, you added the unique_for_date parameter to the slug field.
    👀 This ensures that there will be only one post with a slug for a given date, and thus, you can retrieve single posts using the date and slug.

    👀💡 In the detail view, you use the get_object_or_404() shortcut to retrieve the desired post.

    👀💡 This function retrieves the object that matches the given parameters or an HTTP 404 (not found) exception if no object is found.

    👀 Finally, you use the render() shortcut to render the retrieved post using a template.
"""
