
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receta/new', views.new_receta, name='new_receta'),
    path('receta/edit', views.edit_receta, name='edit_receta'),
]


