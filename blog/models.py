from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категорія")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Кактегорії"



class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата та час")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.URLField(default="http://placehold.it/900x300")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class Comment(models.Model):
    post_name = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, max_length=30, verbose_name="Пост")
    name = models.ForeignKey(User, on_delete=models.CASCADE, max_length=30, verbose_name="Автор")
    data = models.DateTimeField(verbose_name="Дата та час")
    description = models.TextField(max_length=300, verbose_name="Коментар")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
