from django.shortcuts import render
from .models import Member


# Create your views here.


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def champion(request):
    members = Member.objects.all()
    return render(request, 'champion.html', {'members': members})

