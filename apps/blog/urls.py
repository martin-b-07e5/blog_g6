from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]

""" 👀 In the preceding code, you define an application namespace with the app_name variable.
    👀 This allows you to organize URLs by application and use the name when referring to them.

    👀 👀 You define two different patterns using the path() function.
      The first URL pattern doesn't take any arguments and is mapped to the post_list view.
      The second pattern takes the following four arguments and is mapped to the post_detail view:
        - year: Requires an integer
        - month: Requires an integer
        - day: Requires an integer
        - post: Can be composed of words and hyphens

    You use angle brackets to capture the values from the URL.
    Any value specified in the URL pattern as <parameter> is captured as a string.

    You use path converters,
     such as <int:year>, to specifically match and return an integer 
     and <slug:post> to specifically match a slug.

    You can see all path converters provided by Django
    at https://docs.djangoproject.com/en/3.0/topics/http/urls/#path-
    converters.


    If using path() and converters isn't sufficient for you, you can use re_path() instead to define complex URL patterns with Python regular expressions.
    You can learn more about defining URL patterns with regular expressions at https://docs.djangoproject.com/en/3.0/ref/urls/#django.urls.re_path.
    If you haven't worked with regular expressions before,
     you might want to take a look at the Regular Expression HOWTO located at https://docs.python.org/3/howto/regex.html first.
"""

# 💡 Creating a urls.py file for each application is the best way to make your applications reusable by other projects.
