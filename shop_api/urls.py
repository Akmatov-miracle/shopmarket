from django.urls import path
from .views import CategoryListView, CategoryDetailView, FavoriteListView, CartListView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('categories/<str:pk>/', CategoryDetailView.as_view()),
    path('favorites/', FavoriteListView.as_view()),
    path('carts/', CartListView.as_view()),
]