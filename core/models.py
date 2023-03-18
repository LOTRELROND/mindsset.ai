from django.db import models
from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.utils.text import slugify

CustomUser = get_user_model()

class Visiter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    username = models.CharField(max_length=60,null=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(Visiter, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=80, verbose_name="Başlık")
    content = models.TextField(verbose_name="içerik")
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma tarihi")
    active = models.BooleanField(default=True, verbose_name="Yayında")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class FavItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Visiter, on_delete=models.CASCADE, blank=True, default=1)
