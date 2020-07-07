from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('myblog.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]