from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def post_detail(request):
    return render(request, 'post_detail.html')

