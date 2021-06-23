from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from fullstackproject.views import ProductImageViewSet

router = routers.SimpleRouter()
router.register('post_images', ProductImageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/accounts/', include('Accounts.urls')),
    path('api/v1/categories/', include('Category.urls')),
    path('api/v1/products/', include('Products.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)