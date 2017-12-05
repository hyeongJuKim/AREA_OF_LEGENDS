from django.contrib import admin
from .models import Champion
from .models import Skill
from .models import Status

# Register your models here.


class ChampionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Champion._meta.fields]
    search_fields = ('name',)
    list_filter = ('name',)
    # prepopulated_fields = {'area': ('name',)}


admin.site.register(Champion, ChampionAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Skill._meta.fields]
    search_fields = ('name',)

admin.site.register(Skill, SkillAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Status._meta.fields]
    search_fields = ('name',)

admin.site.register(Status, StatusAdmin)


