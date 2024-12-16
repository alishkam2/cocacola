from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DirectorViewSet, MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r"directors", DirectorViewSet, basename="director")
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"reviews", ReviewViewSet, basename="review")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
