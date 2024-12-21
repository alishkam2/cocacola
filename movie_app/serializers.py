from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be greater than 0.")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def validate_stars(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Stars must be between 1 and 5.")
        return value
