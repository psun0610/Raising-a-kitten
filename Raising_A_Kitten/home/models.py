from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=12)
    happiness = models.IntegerField(default=70)
    energy = models.IntegerField(default=70)
    strength = models.IntegerField(default=1)
    body_fat = models.IntegerField(default=10)
    popularity = models.IntegerField(default=0)
    gold = models.IntegerField(default=1000)
    level = models.IntegerField(default=1)
    feed = models.IntegerField(default=1)
    meeting = models.IntegerField(default=0)
    profile = models.ImageField(upload_to='home', null=True)


class Items(models.Model):
    cat_tower = models.CharField(max_length=20)
    work_out = models.CharField(max_length=20)


class Snacks(models.Model):
    name = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)


class Challenge(models.Model):
    name = models.CharField(max_length=50)
    condition = models.TextField(null=True)
    complete = models.BooleanField(default=False)