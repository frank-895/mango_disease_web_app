# Generated by Django 5.1.7 on 2025-04-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mango_disease_app', '0002_authorcard_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorcard',
            name='degree',
            field=models.CharField(default='Computer Science', max_length=30),
        ),
        migrations.AlterField(
            model_name='authorcard',
            name='image',
            field=models.ImageField(default='author_images/default.png', upload_to='author_images/'),
        ),
        migrations.AlterField(
            model_name='authorcard',
            name='interests',
            field=models.CharField(default='No interests', max_length=100),
        ),
    ]
