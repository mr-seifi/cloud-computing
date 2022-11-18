from rest_framework.viewsets import ModelViewSet
from .models import Ad
from .serializers import AdSerializer
from .tasks import push_rabbitmq


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        push_rabbitmq.apply_async(args=(instance.id,))
