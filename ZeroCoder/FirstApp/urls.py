from django.urls import path
from . import views
# . импорт из той папки, в которой находимся


urlpatterns = [
    path('',views.index),
    path('new', views.new)
]
