from django.urls import path

from Like import views
from Like.views import add_like, add_dislike

urlpatterns = [
    path('', views.LikeView.as_view()),
    path('add-like/<int:pk>/', add_like),
    path('add-dislike/<int:pk>/', add_dislike),
]
