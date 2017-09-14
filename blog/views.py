from django.shortcuts import render
from .models import Member, Skill, Status


# Create your views here.


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def champion(request):
    members = Member.objects.all()

    skills = []
    status = []

    for member in members:
        skills.append(Skill.objects.all().filter(member_id=member.id))
        status.append(Status.objects.all().filter(member_id=member.id))

    return render(request,
                  'champion.html',
                  {'members': members, 'skills': skills, 'status': status})

