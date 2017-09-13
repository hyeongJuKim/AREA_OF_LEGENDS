from django.contrib import admin
from .models import Member
from .models import Skill
from .models import Status

# Register your models here.
admin.site.register(Member)
admin.site.register(Skill)
admin.site.register(Status)
