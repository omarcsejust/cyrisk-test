from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Host
from .serializers import HostSerializer


class HostAPIView(APIView, PageNumberPagination):
    def get(self, request, pk=None, format=None):
        host_id = pk
        if host_id is not None:
            # end-point url: /hosts/<int:pk>/
            try:
                host = Host.objects.get(pk=host_id)
            except Host.DoesNotExist:
                host = None
            if host:
                host_serializer = HostSerializer(host)
                return Response(host_serializer.data, status=status.HTTP_200_OK)

            return Response({'message': 'Host not found!'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # paginated hosts list
            # end-point url: /hosts/
            hosts = Host.objects.all()
            res = self.paginate_queryset(hosts, request, view=self)
            serializer = HostSerializer(res, many=True)
            return self.get_paginated_response(serializer.data)
            # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        req_body = request.data
        host_serializer = HostSerializer(data=req_body)
        if host_serializer.is_valid():
            host = host_serializer.save()
            host_serializer = HostSerializer(host)
            return Response(host_serializer.data, status=status.HTTP_201_CREATED)

        return Response(host_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        req_body = request.data
        host_id = pk
        try:
            host = Host.objects.get(pk=host_id)
        except Host.DoesNotExist:
            host = None
        if not host:
            return Response({'message': 'No Host found to update!'}, status=status.HTTP_404_NOT_FOUND)

        host_serializer = HostSerializer(instance=host, data=req_body)
        if host_serializer.is_valid():
            updated_host = host_serializer.save()
            updated_host_serializer = HostSerializer(updated_host)
            return Response(updated_host_serializer.data, status=status.HTTP_200_OK)

        return Response(host_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        host_id = pk
        try:
            host = Host.objects.get(pk=host_id)
        except Host.DoesNotExist:
            host = None
        if not host:
            return Response({'message': 'Host not found!'}, status=status.HTTP_404_NOT_FOUND)

        host.delete()
        return Response({'message': 'Host deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


