# Generated by Django 5.1.7 on 2025-04-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mango_disease_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorcard',
            name='image',
            field=models.ImageField(default='author_images/default.jpg', upload_to='author_images/'),
        ),
    ]
