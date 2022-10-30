from django.urls import path
from . import views

urlpatterns =[
    path('', views.upcoming, name="upcoming"),
    path('trek/<str:hm>/', views.trek, name = "name_treks"),
]