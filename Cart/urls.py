from django.urls import path

from Cart import views

urlpatterns = [
    path('', views.CartListView.as_view()),
    path('create/', views.CartCreateView.as_view()),
    path('delete/<int:pk>/', views.CartDeleteView.as_view()),
]