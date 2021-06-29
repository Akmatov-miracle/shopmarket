from django.urls import path

from Like import views


urlpatterns = [
    path('', views.LikeListView.as_view()),
    path('create/', views.LikeCreateView.as_view()),
    path('delete/<int:pk>/', views.LikeDeleteView.as_view()),
]
