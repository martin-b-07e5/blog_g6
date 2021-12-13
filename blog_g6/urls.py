"""blog_g6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import path
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls', namespace='blog')),
    # 👇🔥🔥🔥 No funciona!! 2021-12-13_13:00:06
    path('apps/blog1/', include('blog1.urls', namespace='blog1')),
]

""" The new URL pattern defined with include refers to the URL patterns defined in the blog application
 so that they are included under the blog/ path.

You include these patterns under the namespace blog.

Namespaces have to be unique across your entire project.

Later, you will refer to your blog URLs easily by using the namespace followed by a colon and the URL name,
 for example, blog:post_list and blog:post_detail.

You can learn more about URL namespaces at https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces.
"""
