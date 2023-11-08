from urllib.parse import unquote
from django.contrib import admin
from django.urls import path,include, re_path
from catalog import views
from django.conf import settings
from django.conf.urls.static import static
from api import views
from world_book.swagger import schema_view

urlpatterns = [
    path('',include('catalog.urls')),
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('api.urls')),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # path('about/', views.about, name='about'),
]

# Настройка для обслуживания медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# д . для регистрации входа пользователей
urlpatterns +=[
    path('accounts/', include('django.contrib.auth.urls')),
]
