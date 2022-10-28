from rest_framework import serializers
from .models import Scan


class AddScanSerializer(serializers.Serializer):
    host = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = '__all__'


