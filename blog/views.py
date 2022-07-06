from django.contrib.auth import forms
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = RegisterForm()
        return render(response, "blog/register.html", {"form":form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    permissions = (
            ("can_add_comment","puede comentar"),
            ("can_view_comment","puede ver comentarios"),
    )

def about_us(request):
    return render(request, "blog/about_us.html")


#---------------------------Filtros -------------------------#

def filter_by_category(request):
    posts = Post.objects.all().order_by('category')
    return render(request, 'blog/post_list.html', {'posts': posts})

def filter_by_category_reverse(request):
    posts = Post.objects.all().order_by('-category')
    return render(request, 'blog/post_list.html', {'posts': posts})

def filter_by_title(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'blog/post_list.html', {'posts': posts})

def filter_by_title_reverse(request):
    posts = Post.objects.all().order_by('-title')
    return render(request, 'blog/post_list.html', {'posts': posts})

def filter_by_publish(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def filter_by_publish_reverse(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def filter_by_number_of_comments(request):
    posts = Post.objects.raw('SELECT blog_post.*, (SELECT count(*) FROM blog_comment WHERE blog_comment.post_id = blog_post.id) AS comentario FROM blog_post ORDER BY comentario DESC LIMIT 3')
    return render(request, 'blog/post_list.html', {'posts': posts})