from django.db import models
from django.utils import timezone

from accounts.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name of category")

    def __str__(self):
        return f'{self.name}'


class Advertisement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, verbose_name="Title of advertisement")
    content = models.TextField(max_length=500, verbose_name="Content of advertisement")
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True, verbose_name="Picture")
    publication_date = models.DateField(default=timezone.now, verbose_name="Date of publication")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price, rub")

    def __str__(self):
        return f'{self.user} {self.title}'


class Message(models.Model):
    target_ad = models.ForeignKey(Advertisement, on_delete=models.DO_NOTHING)
    publication_date = models.DateField(default=timezone.now, verbose_name="Date of publication")
    text = models.TextField(max_length=300)

