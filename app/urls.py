from django.urls import path
from . import views


urlpatterns = [
    path('', views.choice_of_operation, name='choice of operation'),
    path('<selected_operation>/', views.enter_numbers, name='selected operation'),
    path('<selected_operation>/result/', views.calculate, name='result')
]
