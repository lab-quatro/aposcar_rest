from django.db import models


class Nominee(models.Model):
    name = models.TextField()
    picture_url = models.ImageField(upload_to='nominees/')
    description = models.TextField()

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
    annotation = models.TextField()
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return f'"{self.nominated.name}" on "{self.category.name}"'