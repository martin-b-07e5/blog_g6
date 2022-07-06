from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views import CustomLoginView  
from blog.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include("django.contrib.auth.urls")),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='blog/login.html',authentication_form=LoginForm), name='login'),
    
]