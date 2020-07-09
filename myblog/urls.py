from django.urls import path, include

from rest_framework.routers import DefaultRouter

from myblog import views


router = DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
