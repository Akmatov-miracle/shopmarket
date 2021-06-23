from django.urls import path
from . import views
from .views import CategoryCreateView, CategoryDetailView

urlpatterns = [
    path('', views.CategoryView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('<int:pk>/', CategoryDetailView.as_view()),
    # path('<int:pk>/', views.CategoryDetailView.as_view()),
]
