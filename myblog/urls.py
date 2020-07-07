from django.urls import path
from myblog import views

urlpatterns = [
    path('tags/', views.tag_list),
    path('tags/<int:pk>/', views.comment_detail),
    path('posts/', views.post_list),
    path('posts/<int:pk>/', views.post_detail),
    path('comments/', views.comment_list),
    path('comments/<int:pk>/', views.comment_detail),
]