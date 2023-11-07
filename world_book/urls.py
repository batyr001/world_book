from urllib.parse import unquote
from django.contrib import admin
from django.urls import path,include
from catalog import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('catalog.urls')),
    path('admin/', admin.site.urls),
    # path('about/', views.about, name='about'),
]
# urls.py


# Настройка для обслуживания медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# д . для регистрации входа пользователей
urlpatterns +=[
    path('accounts/', include('django.contrib.auth.urls')),
]