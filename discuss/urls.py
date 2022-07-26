from django.urls import path

from discuss import views
urlpatterns =[

    path('add_comment/<int:pk>/', views.add_comments, name='comment')
]