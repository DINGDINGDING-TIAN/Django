from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myblog import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('tags/', views.TagList.as_view(), name='tags-list'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags-detail'),
    path('tags/<int:pk>/highlight/', views.TagHighlight.as_view(), name='tags-highlight'),
    path('comments/', views.CommentList.as_view(), name='comments-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comments-detail'),
    path('comments/<int:pk>/highlight/', views.CommentHighlight.as_view(), name='comments-highlight'),
    path('posts/', views.PostList.as_view(), name='posts-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts-detail'),
    path('posts/<int:pk>/highlight/', views.PostHighlight.as_view(), name='posts-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
])
