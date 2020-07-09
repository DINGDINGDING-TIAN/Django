from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
