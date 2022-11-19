from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .models import Ad, User
from .serializers import AdSerializer, UserSerializer
from .tasks import push_rabbitmq


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        push_rabbitmq.apply_async(args=(instance.id,))
