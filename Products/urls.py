
from django.urls import path
from Products import views


urlpatterns = [
    path('', views.api_overview_links),
    path('posts/List/', views.ProductListView.as_view(), name='list'),
    path('posts/<int:pk>/detail/', views.ProductDetailView.as_view(), name='detail'),
    path('posts/create/', views.ProductCreateView.as_view(), name='create'),
    path('posts/<int:pk>/update/', views.ProductUpdateView.as_view(), name='update'),
    path('posts/<int:pk>/delete/', views.ProductDeleteView.as_view()),
    # path('posts/Like/', views.LikeListView.as_view(), name='like'),




]