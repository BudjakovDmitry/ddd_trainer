from rest_framework import serializers

from adapty_app.infrastructure.models.models import User, Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    device_info = DeviceSerializer

    class Meta:
        model = User
        fields = '__all__'
