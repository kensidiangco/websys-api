from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .models import Review
from .serializers import ReviewCreateSerializer, ReviewSerializer
from rest_framework.response import Response

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all().order_by('-date_created')
    serializer_class = ReviewSerializer

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer

class ReviewRetrieveView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDeleteView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewUpdateView(generics.UpdateAPIView):
    lookup_field = "id"
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer