# Generated by Django 3.1.7 on 2021-02-19 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_book_cover_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
