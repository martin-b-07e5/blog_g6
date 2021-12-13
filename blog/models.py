from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# add the custom manager:
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
            .filter(status='published')

""" 👀 The first manager declared in a model becomes the default manager.
    You can use the Meta attribute default_manager_name to specify a different default manager.
    If no manager is defined in the model, Django automatically creates the objects default manager for it.
    ✍💡 If you declare any managers for your model but you want to keep the objects manager as well, you have to add it explicitly to your model.
    ✍💡 In the preceding code, you add the default objects manager and the published custom manager to the Post model.
    👀 The get_queryset() method of a manager returns the QuerySet that will be executed.
    👀 You override this method to include your custom filter in the final QuerySet.
"""

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()    # The default manager. 👀
    published = PublishedManager()    # Our custom manager. 👀👀

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # 👀 You will use the get_absolute_url() method in your templates to link to specific posts.
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])


""" slug: This is a field intended to be used in URLs.
          A slug is a short label that contains only letters, numbers, underscores, or hyphens.
          You will use the slug field to build beautiful, SEO-friendly URLs for your blog posts.
            You have added the unique_for_date parameter to this field so that you can build URLs for posts using their publish date and slug.
            Django will prevent multiple posts from having the same slug for a given date.

    author: This field defines a many-to-one relationship, meaning that each post is written by a user, and a user can write any number of posts.
            For this field, Django will create a foreign key in the database using the primary key of the related model.
            In this case, you are relying on the User model of the Django authentication system.
            The on_delete parameter specifies the behavior to adopt when the referenced object is deleted.
            This is not specific to Django; it is an SQL standard.
                Using CASCADE, you specify that when the referenced user is deleted, the database will also delete all related blog posts.
                    You can take a look at all the possible options at https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.on_delete.
                You specify the name of the reverse relationship, from User to Post, with the related_name attribute.
                This will allow you to access related objects easily.

    body: This is the body of the post.
          This field is a text field that translates into a TEXT column in the SQL database.

    publish: This datetime indicates when the post was published.
             You use Django's timezone now method as the default value.
             This returns the current datetime in a timezone-aware format.
             You can think of it as a timezone-aware version of the standard Python datetime.now method.

    created: This datetime indicates when the post was created.
            Since you are using auto_now_add here, the date will be saved automatically when creating an object.

    updated: This datetime indicates the last time the post was updated.

    status: This field shows the status of a post.
            You use a choices parameter, so the value of this field can only be set to one of the given choices.
"""


""" A canonical URL is the preferred URL for a resource.
    👀 You may have different pages in your site where you display posts, but there is a single URL that you use as the main URL for a blog post.
    The convention in Django is to add a get_absolute_url() method to the model that returns the canonical URL for the object.

    👀💡 You can use the post_detail URL that you have defined in the preceding section to build the canonical URL for Post objects.
    👀💡For this method, you will use the reverse() method, which allows you to build URLs by their name and pass optional parameters.
    You can learn more about the URLs utility functions at https://docs.djangoproject.com/en/3.0/ref/urlresolvers/.

    👀 You will use the get_absolute_url() method in your templates to link to specific posts.
"""