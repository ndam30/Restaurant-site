from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menus, name='menu'),
    path('food/<id>', views.foods, name='food'),
    path('special', views.smeal, name= 'special'),
    path('team', views.teams, name= 'team'),
    path('search/', views.search, name='search')
]