from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('welcome/', views.welcome),
    path('show-persons/', views.show_person),
    path('person/<int:id>/', views.person),
]