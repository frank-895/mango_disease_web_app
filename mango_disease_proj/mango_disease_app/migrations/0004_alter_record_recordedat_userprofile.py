# Generated by Django 5.2 on 2025-05-07 07:19

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mango_disease_app', '0003_alter_disease_controlmethod_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='recordedAt',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('student_number', models.CharField(max_length=7)),
                ('degree', models.CharField(max_length=30)),
                ('interests', models.CharField(max_length=100)),
                ('image', models.ImageField(default='author_images/blank.png', upload_to='author_images/')),
                ('collaborator_independent', models.SmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('bigPicture_detailOriented', models.SmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('communicator_listener', models.SmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('creative_practical', models.SmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('user', models.OneToOneField(limit_choices_to={'is_superuser': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
