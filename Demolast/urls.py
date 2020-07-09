from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('', include('myblog.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]