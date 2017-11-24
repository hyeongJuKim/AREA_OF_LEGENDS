"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import DetailView
from django.views.generic import ListView

from blog.models import Champion
from . import views


urlpatterns = [

    url(r'^$', views.main, name='main'),
    url(r'^about$', views.about, name='about'),
    url(r'^champion/', views.champion, name='champion'),

    # vies.py없이 간단히 만들수도 있다.
    url(r'^champions/$', ListView.as_view(model=Champion), name='champion_list'),
    url(r'^champions/(?P<pk>\d+)/$', DetailView.as_view(model=Champion), name='champion_detail'),

]
