from django.urls import path
from .views import (
    DirectorListCreateView, DirectorDetailView,
    MovieListCreateView, MovieDetailView, MovieWithReviewsView,
    ReviewListCreateView, ReviewDetailView
)

urlpatterns = [
    path('directors/', DirectorListCreateView.as_view(), name='directors-list'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('movies/', MovieListCreateView.as_view(), name='movies-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/reviews/', MovieWithReviewsView.as_view(), name='movies-reviews'),
    path('reviews/', ReviewListCreateView.as_view(), name='reviews-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
