from django.urls import path
from . import views

urlpatterns = [
    path('<int:card>', views.add_sum, name='add_sum'),
    path('', views.index, name='index'),
]
