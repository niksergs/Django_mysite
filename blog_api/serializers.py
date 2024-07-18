from rest_framework import serializers
from blog.models import (Post,
                         Comment,
                         )


class CommentSerializer(serializers.Serializer):
    """Serializer для модели Comment на основе базового сириализатора"""
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance


class PostSerializer(serializers.ModelSerializer):
    """Serializer для модели Post на основе ModelSerializer"""
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'created']
