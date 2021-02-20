# Generated by Django 3.1.7 on 2021-02-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_type',
            field=models.CharField(choices=[('Мягкая', 'Мягкая'), ('Твёрдая', 'Твёрдая')], default='Мягкая', max_length=10),
        ),
    ]