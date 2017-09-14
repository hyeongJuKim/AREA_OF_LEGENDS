from django.db import models


# Create your models here.
class Champion(models.Model):
    champion_name = models.CharField(max_length=30)
    champion_area = models.CharField(max_length=100)
    profile_img = models.CharField(max_length=200)

    def __str__(self):
        return self.champion_name


class Skill(models.Model):
    champion = models.ForeignKey(Champion,
                                 related_name='skills',
                                 on_delete=models.CASCADE)
    skill_no = models.IntegerField(blank=True)
    skill_name = models.TextField(max_length=1000, blank=True)
    skill_url = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.skill_name


class Status(models.Model):
    champion = models.ForeignKey(Champion,
                                 related_name='status',
                                 on_delete=models.CASCADE)
    status_no = models.IntegerField(blank=True)
    status_name = models.CharField(max_length=30, blank=True)
    status_point = models.IntegerField(blank=True)

    def __str__(self):
        return self.status_name
