
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from shop_api.views import MovieViewSet, ReviewViewSet

schema_view = get_schema_view(
    info=openapi.Info(
        title='Blog Project',
        default_version='v1',
        description='this is test blog project',
        terms_of_service='http://www.google.com/policies/terms/',
        contact=openapi.Contact(email='test@gmail.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

router = DefaultRouter()
router.register('product', MovieViewSet)
router.register('review', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/docs/', schema_view.with_ui()),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/accounts/', include('user.urls'),),
    path('api/v1/profile/', include('product_profile.urls')),
    path('api/v1/', include('shop_api.urls')),
    path('api/v1/', include(router.urls)),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
