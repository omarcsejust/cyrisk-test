from rest_framework import serializers
from .models import Tag
import json


class TagSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField('get_categories_list')
    versions = serializers.SerializerMethodField('get_versions_list')

    def get_categories_list(self, obj):
        return json.loads(obj.categories)

    def get_versions_list(self, obj):
        return json.loads(obj.versions)

    class Meta:
        model = Tag
        # fields = ['id', 'name', 'created', 'categories', 'versions']
        fields = '__all__'


class TagSerializerCalc(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField('get_categories_list')
    versions = serializers.SerializerMethodField('get_versions_list')
    found_in_scans_count = serializers.SerializerMethodField('get_scans_count')

    def get_categories_list(self, obj):
        return json.loads(obj.categories)

    def get_versions_list(self, obj):
        return json.loads(obj.versions)

    def get_scans_count(self, obj):
        return len(obj.scan_set.all())

    def get_hosts_count(self, obj):
        # TODO:: have plan to do it later
        pass

    class Meta:
        model = Tag
        fields = '__all__'  # all means --> additional calculated fields also
