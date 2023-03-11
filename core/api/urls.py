from django.urls import path
from core.api import views as api_views

urlpatterns = [
    path('post/',api_views.PostListCreateAPIView.as_view(),name="post-list"),
    path('post/<int:pk>/',api_views.PostDetailAPIView.as_view(), name="post-edit"),
]
