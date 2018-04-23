from rest_framework import serializers
from .models import Tweet


class HomeTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'


class PostUpdateSerializer(serializers.Serializer):
    tweet = serializers.CharField()

    def validate_tweet(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("tweet is too short.")
        return value

