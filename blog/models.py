from django.db import models


# Create your models here.
class Champion(models.Model):
    name = models.CharField(max_length=30)
    profile = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    profile_img = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Skill(models.Model):
    champion = models.ForeignKey(Champion,
                                 related_name='skills',
                                 on_delete=models.CASCADE)
    no = models.IntegerField(blank=True)
    name = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    champion = models.ForeignKey(Champion,
                                 related_name='status',
                                 on_delete=models.CASCADE)
    no = models.IntegerField(blank=True)
    name = models.CharField(max_length=30, blank=True)
    point = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
