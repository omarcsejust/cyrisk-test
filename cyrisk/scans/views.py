from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from hosts.models import Host
from .models import Scan
from .serializers import *
from .background_analyzer import analyze


class ScanAPIView(APIView, PageNumberPagination):
    def get(self, request, pk=None, format=None):
        scan_id = pk
        if scan_id is not None:
            # end-point url: /scans/<int:pk>/
            try:
                scan = Scan.objects.get(pk=scan_id)
            except Scan.DoesNotExist:
                scan = None
            if scan:
                scan_serializer = ScanSerializer(scan)
                return Response(scan_serializer.data, status=status.HTTP_200_OK)

            return Response({'message': 'Scan not found!'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # paginated scans list
            # end-point url: /scans/
            scans = Scan.objects.all()
            res = self.paginate_queryset(scans, request, view=self)
            serializer = ScanSerializer(res, many=True)
            return self.get_paginated_response(serializer.data)
            # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        req_body = request.data
        add_scan_serializer = AddScanSerializer(data=req_body)
        if add_scan_serializer.is_valid():
            try:
                host = Host.objects.get(pk=add_scan_serializer.data.get('host'))
            except Host.DoesNotExist:
                host = None
            if not host:
                return Response({'message': 'Host not found!'}, status=status.HTTP_404_NOT_FOUND)

            scan = Scan.objects.filter(host=host)
            if scan:
                # scan already exists
                serializer = ScanSerializer(scan[0])
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # create scan & trigger background task
                new_scan = Scan.objects.create(host=host)
                serializer = ScanSerializer(new_scan)
                analyze(new_scan.id, host.domain)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(add_scan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        scan_id = pk
        try:
            scan = Scan.objects.get(pk=scan_id)
        except Scan.DoesNotExist:
            scan = None
        if not scan:
            return Response({'message': 'Scan not found!'}, status=status.HTTP_404_NOT_FOUND)

        scan.delete()
        return Response({'message': 'Scan deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


