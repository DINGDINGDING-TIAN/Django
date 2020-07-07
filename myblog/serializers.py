from rest_framework import serializers
from myblog.models import Tag, Post, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer()

    class Meta:
        model = Post
        fields = ['title', 'summary', 'content', 'published_at', 'author', 'tags']


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = ['post', 'content', 'published_at', 'author']
