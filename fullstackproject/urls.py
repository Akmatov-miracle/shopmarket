from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from fullstackproject.views import ProductImageViewSet

router = routers.SimpleRouter()
router.register('post_images', ProductImageViewSet)

schema_view = get_schema_view(
    info=openapi.Info(
        title="SHOP MARKET",
        default_version='v1',
        description='this is shop market project',
        terms_of_service='http://www.google.com/policies/terms/',
        contact=openapi.Contact(email='test@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/accounts/', include('Accounts.urls')),
    path('api/v1/categories/', include('Category.urls')),
    path('api/v1/products/', include('Products.urls')),
    path('api/v1/comments/', include('Comments.urls')),
    path('api/v1/like/', include('Like.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)