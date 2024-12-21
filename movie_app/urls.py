from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DirectorViewSet, MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register("directors", DirectorViewSet)
router.register("movies", MovieViewSet)
router.register("reviews", ReviewViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
