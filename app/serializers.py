from dataclasses import field
from tkinter.messagebox import QUESTION
from rest_framework import serializers
from .models import Review, Vote

class ReviewSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format="%b %d %Y, %I:%M %p")
    date_updated = serializers.DateTimeField(format="%b %d %Y, %I:%M %p")
    class Meta:
        model = Review
        fields = ('name', 'email', 'topic', 'message', 'date_created', 'date_updated')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('up_votes', 'down_votes', 'email')

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('name', 'email', 'topic', 'message')