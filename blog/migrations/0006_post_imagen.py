# Generated by Django 3.2.9 on 2021-12-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default=False, upload_to='', verbose_name=False),
            preserve_default=False,
        ),
    ]
