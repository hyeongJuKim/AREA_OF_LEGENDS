from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Champion, Skill, Status


# Create your views here.


def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')


def champion(request):
    champions = Champion.objects.all()
    show_list = []
    for champ in champions:
        champ_dict = dict()
        champ_dict.update(
            {'champion': Champion.objects.all().filter(id=champ.id)})
        champ_dict.update(
            {'skill_list': Skill.objects.all().filter(champion_id=champ.id)})
        champ_dict.update(
            {'status_list': Status.objects.all().filter(champion_id=champ.id)})
        show_list.append(champ_dict)

    return render(request,
                  'champion.html',
                  {'champions': champions, 'show_list': show_list})


class ChampionLV(ListView):
    model = Champion


class ChampionDV(DetailView):
    model = Champion



