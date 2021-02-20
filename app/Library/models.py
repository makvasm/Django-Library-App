from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    country    = models.CharField(max_length=255)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    class CoverType(models.TextChoices):
        SOFT = 'Мягкая', 'Мягкая'
        HARD = 'Твёрдая', 'Твёрдая'

    author     = models.ForeignKey(Author, on_delete=models.CASCADE)
    cover_type = models.CharField(
        choices=CoverType.choices,
        default=CoverType.SOFT,
        max_length=10
    )
    title      = models.CharField(max_length=255)
    publisher  = models.CharField(max_length=255)
    page_count = models.PositiveIntegerField()
    pub_date   = models.DateField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
