from django.urls import path
from . import views

urlpatterns= [
    path("reviews/", views.ReviewListView.as_view(), name="review"),
    path("review/create", views.ReviewCreateView.as_view(), name="review-create"),
    path("review/<int:id>", views.ReviewRetrieveView.as_view(), name="review-retrieve"),
    path("review/delete/<int:id>", views.ReviewDeleteView.as_view(), name="review-delete"),
    path("review/update/<int:id>", views.ReviewUpdateView.as_view(), name="review-update"),
]