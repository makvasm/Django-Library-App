# Generated by Django 3.1.7 on 2021-02-20 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0004_auto_20210219_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pub_year',
            new_name='pub_date',
        ),
    ]