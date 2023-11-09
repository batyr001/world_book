from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,GenreViewSet,LanguageViewSet,PublisherViewSet,AuthorViewSet,StatusViewSet,BookInstanceViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'Language ', LanguageViewSet)
router.register(r'publisher ', PublisherViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'status', StatusViewSet)
router.register(r'bookInstance', BookInstanceViewSet)




urlpatterns = [
    path('', include(router.urls)),
    # Add other URL patterns for your app as needed
]

