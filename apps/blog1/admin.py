from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # list_display = ('title', 'slug', 'author', 'publish')
    # list_display = ('title', 'slug', 'author')
    # list_display = ('title', 'slug')    # both required

    list_filter = ('status', 'created', 'publish', 'author')
    # list_filter = ('status', 'created', 'publish')
    # list_filter = ('status', 'created')    # both required

    search_fields = ('title', 'body')    # Search in the title and body

    prepopulated_fields = {'slug': ('title',)}    # As you type the title of a new post, the slug field is filled in automatically.

    raw_id_fields = ('author',)    # the author field is now displayed with a lookup widget

    date_hierarchy = 'publish'    # agrega para filtrar top left below search

    ordering = ('status', 'publish')    # Order by status, then by publish.



"""You are telling the Django administration site
     that your model is registered in the site
      using a custom class
       that inherits from ModelAdmin.
    
    In this class, you can include information about
     how to display the model in the site and
      how to interact with it.
    
    The list_display attribute
     allows you to set the fields of your model
      that you want to display on the administration object list page.

    The
     @admin.register() decorator
      performs the same function as the
       admin.site.register() function
        that you replaced,
      registering the ModelAdmin class that it decorates.


    As you type the title of a new post, the slug field is filled in automatically.
    You have told Django to prepopulate the slug field with the input of the title field using the prepopulated_fields attribute.
    
    Also, the author field is now displayed with a lookup widget that can scale much better than a drop-down select input when you have thousands of users.
    This is achieved with the raw_id_fields attribute
"""