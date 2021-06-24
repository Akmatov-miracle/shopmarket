from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentListCreateView.as_view()),
    path('<int:pk>/', views.CommentDetailView.as_view()),
]