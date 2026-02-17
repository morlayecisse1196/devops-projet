from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from gestion.models.histoire import Histoire
from gestion.serializers.histoire_serializer import (
    HistoireSerializer,
    SaveHistoireSerializer,
    UpdateHistoireSerializer
)
from gestion.services.histoire_service import HistoireService


class HistoireAPIView(generics.GenericAPIView):
    """GET toutes les histoires, POST créer une histoire"""
    permission_classes = [IsAuthenticated]
    queryset = Histoire.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveHistoireSerializer
        return HistoireSerializer

    def get(self, request):
        histoires = HistoireService.get_all()
        serializer = HistoireSerializer(histoires, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        histoire = HistoireService.create(serializer.validated_data)
        return Response(
            {"message": "Histoire créée avec succès", "id": histoire.id},
            status=status.HTTP_201_CREATED
        )


class HistoireDetailAPIView(generics.GenericAPIView):
    """GET by id, PUT, DELETE"""
    permission_classes = [IsAuthenticated]
    queryset = Histoire.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateHistoireSerializer
        return HistoireSerializer

    def get(self, request, id):
        histoire = HistoireService.get_by_id(id)
        serializer = HistoireSerializer(histoire)
        return Response(serializer.data)

    def put(self, request, id):
        histoire = HistoireService.get_by_id(id)
        serializer = self.get_serializer(histoire, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        histoire = HistoireService.update(histoire, serializer.validated_data)
        return Response(HistoireSerializer(histoire).data)

    def delete(self, request, id):
        histoire = HistoireService.get_by_id(id)
        HistoireService.delete(histoire)
        return Response(status=status.HTTP_204_NO_CONTENT)
