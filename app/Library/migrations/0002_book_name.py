# Generated by Django 3.1.7 on 2021-02-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='book', max_length=255),
            preserve_default=False,
        ),
    ]
