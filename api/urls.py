from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)


urlpatterns = [
    path('api-auth/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
