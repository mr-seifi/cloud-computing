from django.urls import path, include
from .views import AdViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ad', AdViewSet)

urlpatterns = [
    path('', include(router.urls))
]
