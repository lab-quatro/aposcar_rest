from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


class Nominee(models.Model):
    name = models.TextField()
    picture = models.ImageField(upload_to='nominees/')

    class Meta:
        verbose_name_plural = 'nominees'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Indication(models.Model):
    nominated = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.IntegerField()
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return f'"{self.nominated.name}" on "{self.category.name}"'


class UserProfile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    bets = models.ManyToManyField(Indication)

    def __str__(self):
        return self.username


class Room(models.Model):
    share_code = models.CharField(unique=True, max_length=6, blank=True)
    name = models.CharField(max_length=14)
    owner = models.ForeignKey(UserProfile, related_name='owner', on_delete=models.CASCADE)
    users = models.ManyToManyField(UserProfile, related_name='users', blank=True)

    def save(self, *args, **kwargs):
        share_code = self.share_code
        if not share_code:
            share_code = uuid.uuid4().hex[:6].upper()
        while Room.objects.filter(share_code=share_code).exclude(pk=self.pk).exists():
            share_code = uuid.uuid4().hex[:6].upper()
        self.share_code = share_code
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
