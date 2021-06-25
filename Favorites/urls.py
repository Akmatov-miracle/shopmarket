from django.urls import path

from Favorites.views import FavoriteListView

urlpatterns = [
    path('favorites/', FavoriteListView.as_view()),
]