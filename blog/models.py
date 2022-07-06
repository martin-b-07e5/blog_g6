from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count


class Post(models.Model):
    CATEGORIES_CHOICES = (
        ('Fin de la Pobreza' , 'Fin de la pobreza'),
        ('Hambre Cero' ,'Hambre Cero'),
        ('Salud y Bienestar' ,'Salud y Bienestar'),
        ('Educación de Calidad', 'Educación de Calidad'),
        ('Igualdad de Género', 'Igualdad de Género'),
        ('Agua limpia y Saneamiento', 'Agua limpia y Saneamiento'),
        ('Energía asequible y no contaminante', 'Energía asequible y no contaminante'),
        ('Trabajo Decente', 'Trabajo Decente'),
        ('Industria,Innovacion e Infraestructura', 'Industria,Innovacion e Infraestructura'),
        ('Reducción de las Desigualdades', 'Reducción de las Desigualdades'),
        ('Ciudades Sostenibles', 'Ciudades Sostenibles'),
        ('Producción y Consumo Responsable', 'Producción y Consumo Responsable'),
        ('Acción por el Clima' , 'Acción por el Clima'),
        ('Vida Sumbarina' , 'Vida Submarina'),
        ('Vida de Ecosistemas Terrestres' , 'Vida de Ecosistemas Terrestres'),
        ('Paz y Justicia' , 'Paz y Justicia'),
        ('Alianzas para lograr los objetivos' , 'Alianzas para lograr los objetivos')
           )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True,upload_to="media/" )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.CharField(
        max_length=120,
        choices=CATEGORIES_CHOICES,
        default='sin categoria'
        )

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, verbose_name= "Autor")
    text = models.TextField(verbose_name="Comentario")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

