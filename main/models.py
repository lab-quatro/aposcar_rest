from django.db import models
from django.contrib.auth.models import User

import uuid


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return f"{self.user.username}'s profile"


class Nominee(models.Model):
    name = models.TextField()
    picture = models.ImageField()

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
    year = models.DateField()
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return f'"{self.nominated.name}" on "{self.category.name}"'


class Bet(models.Model):
    indication = models.ForeignKey(Indication, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Room(models.Model):
    share_code = models.CharField(unique=True, max_length=6, blank=True)
    name = models.CharField(max_length=14)
    profile_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        share_code = self.share_code
        if not share_code:
            share_code = uuid.uuid4().hex[:6].upper()
        while Room.objects.filter(share_code=share_code).exclude(pk=self.pk).exists():
            share_code = uuid.uuid4().hex[:6].upper()
        self.systemCode = share_code
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class JoinedRoom(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
