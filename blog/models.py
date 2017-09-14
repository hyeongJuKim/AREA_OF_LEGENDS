from django.db import models


# Create your models here.
class Member(models.Model):
    member_name = models.CharField(max_length=30)
    member_area = models.CharField(max_length=100)
    profile_img = models.CharField(max_length=200)

    def __str__(self):
        return self.member_name


class Skill(models.Model):
    member = models.ForeignKey(Member
                               , related_name='skills'
                               , on_delete=models.CASCADE)
    skill_no = models.IntegerField()
    skill_name = models.TextField(max_length=1000)

    def __str__(self):
        return self.skill_name


class Status(models.Model):
    member = models.ForeignKey(Member
                               , related_name='status'
                               , on_delete=models.CASCADE)
    status_no = models.IntegerField()
    status_name = models.CharField(max_length=30)
    status_point = models.IntegerField()

    def __str__(self):
        return self.status_name
