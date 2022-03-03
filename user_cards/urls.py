from django.urls import path
from . import views

urlpatterns = [
    path('add_card', views.add_card, name='add_card'),
    path('<int:card>', views.add_sum, name='add_sum'),
    path('', views.index, name='index'),
]
