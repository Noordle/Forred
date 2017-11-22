from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    date = models.DateTimeField('Дата публикации')
    message = models.TextField('Текст публикации', max_length=10000)
    author = models.ForeignKey(User)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/posts/%i" % self.id


class Comment(models.Model):
    author = models.ForeignKey(User)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    text = models.TextField(max_length=10000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text