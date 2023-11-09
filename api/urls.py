from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,GenreViewSet,LanguageViewSet,PublisherViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'Language ', LanguageViewSet)
router.register(r'publisher ', PublisherViewSet)




urlpatterns = [
    path('', include(router.urls)),
    # Add other URL patterns for your app as needed
]

