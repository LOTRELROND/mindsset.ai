from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('updateFav/', views.updateFav, name = 'updateFav'),
    path('fav/', views.fav, name = 'fav'),
    path('createvisitor/', views.createvisitor, name = 'createvisitor'),
]
