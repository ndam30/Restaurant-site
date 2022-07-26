from django.urls import path

from accounts import views

urlpatterns=[
    path('accounts/', views.registration ,name ='register'),
    path('login', views.login , name ='login'),
    path('', views.logout1, name='logout'),
    path('dashboard', views.dashboard , name ='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('reserve/', views.reservation, name='reserve'),

]