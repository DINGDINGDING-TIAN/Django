from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=70)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Comment on {self.post} from {self.author}, published at {self.published_at}'

    class Meta:
        ordering = ['published_at']


author = models.ForeignKey('auth.User', related_name='myblog', on_delete=models.CASCADE)


def save(self, *args, **kwargs):
    super(Post, self).save(*args, **kwargs)


def save(self, *args, **kwargs):
    super(Tag, self).save(*args, **kwargs)


def save(self, *args, **kwargs):
    super(Comment, self).save(*args, **kwargs)