# Generated by Django 5.2 on 2025-05-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mango_disease_app', '0007_disease_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='image',
            field=models.ImageField(default='disease_images/default.JPG', upload_to='disease_images/'),
        ),
    ]
