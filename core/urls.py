from django.urls import path, include
from .views import AdViewSet, UserCreateAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ad', AdViewSet)

urlpatterns = [
    path('user/', UserCreateAPIView.as_view()),
    path('', include(router.urls))
]
