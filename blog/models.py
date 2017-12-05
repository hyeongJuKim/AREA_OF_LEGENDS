from django.db import models


# Create your models here.
class Champion(models.Model):
    name = models.CharField(max_length=30, help_text='챔피언의 이름을 입력하세요.')
    area = models.CharField(max_length=100, help_text='주로 생활하는 지역을 입력하세요.')
    profile = models.CharField(max_length=100, help_text='챔피언의 종족을 입력하세요.')
    profile_img = models.CharField(max_length=200, help_text='프로필 이미지의 url을 입력하세요.')
    background_story = models.TextField(max_length=500, blank=True, help_text='챔피언의 배경 이야기를 입력하세요.')
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    modify_date = models.DateTimeField(auto_now=True, blank=True)

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
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    modify_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    champion = models.ForeignKey(Champion,
                                 related_name='status',
                                 on_delete=models.CASCADE)
    no = models.IntegerField(blank=True)
    name = models.CharField(max_length=30, blank=True)
    point = models.IntegerField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
