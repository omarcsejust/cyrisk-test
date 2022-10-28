from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Tag
from .serializers import *


class TagAPIView(APIView, PageNumberPagination):
    def get(self, request, pk=None, format=None):
        tag_id = pk
        if tag_id is not None:
            # end-point url: /tags/<int:pk>/
            try:
                tag = Tag.objects.get(pk=tag_id)
            except Tag.DoesNotExist:
                tag = None
            if tag:
                tag_serializer = TagSerializerCalc(tag)
                return Response(tag_serializer.data, status=status.HTTP_200_OK)

            return Response({'message': 'Tag not found!'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # paginated tags list
            # end-point url: /tags/
            tags = Tag.objects.all()
            res = self.paginate_queryset(tags, request, view=self)
            serializer = TagSerializer(res, many=True)
            return self.get_paginated_response(serializer.data)
            # return Response(serializer.data, status=status.HTTP_200_OK)




