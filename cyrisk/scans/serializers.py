from rest_framework import serializers
from .models import Scan
from tags.serializers import TagSerializer


class AddScanSerializer(serializers.Serializer):
    host = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ScanSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Scan
        fields = '__all__'


class ApiTestSerializer(serializers.Serializer):
    is_active = serializers.BooleanField(required=False, default=False)


