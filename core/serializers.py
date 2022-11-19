from rest_framework.serializers import ModelSerializer
from .models import Ad, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', )


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'title', 'description', 'cover', 'user', 'approved',)
        read_only_fields = ('approved',)
