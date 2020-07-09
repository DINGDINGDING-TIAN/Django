from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Tag, Post, Comment


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ['name']


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ['post', 'content', 'published_at', 'author']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.HyperlinkedRelatedField(many=True, view_name='tags', queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'summary', 'content', 'published_at', 'author', 'tags']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comments', read_only=True)
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='posts', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'comments', 'posts']