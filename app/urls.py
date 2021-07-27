from django.urls import path
from . import views


urlpatterns = [
    path('', views.choice_of_operation, name='choice_of_operation'),
    path('<selected_operation>/', views.enter_numbers, name='selected_operation'),
    path('<selected_operation>/result/', views.calculate, name='result')
]
