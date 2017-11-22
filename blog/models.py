from django.db import models


class Post(models.Model):
    title = models.CharField(u"Çàãîëîâîê", max_length=255)
    date = models.DateTimeField(u'Äàòà ïóáëèêàöèè')
    message = models.TextField(u'Òåêñò ñîîáùåíèÿ', max_length=10000)
    author = models.CharField(u'Èìÿ àâòîðà', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/posts/%i" % self.id


class Comment(models.Model):
    author = models.CharField(max_length=100)
    date = models.DateTimeField(u'Äàòà ïóáëèêàöèè', auto_now_add=True)
    text = models.TextField(max_length=10000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text