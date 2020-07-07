from rest_framework import serializers
from myblog.models import Tag, Post, Comment
from django.contrib.auth.models import User


class TagSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='tags-highlight', format='html')

    class Meta:
        model = Tag
        fields = ['name']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='comments-highlight', format='html')

    class Meta:
        model = Tag
        fields = ['post', 'content', 'published_at', 'author']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='posts-highlight', format='html')

    class Meta:
        model = Post
        fields = ['title', 'summary', 'content', 'published_at', 'author', 'tags']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.HyperlinkedRelatedField(many=True, view_name='tags-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comments-detail', read_only=True)
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='posts-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'tags', 'comments', 'posts']