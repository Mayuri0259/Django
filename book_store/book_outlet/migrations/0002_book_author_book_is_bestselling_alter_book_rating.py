# Generated by Django 5.1.4 on 2024-12-24 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
