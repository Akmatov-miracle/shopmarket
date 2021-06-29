from django.urls import path
from . import views

urlpatterns = [
    path('', views.FavoritesListView.as_view()),
    path('create/', views.FavoritesCreateView.as_view()),
    path('delete/<int:pk>/', views.FavoritesDeleteView.as_view()),
]
