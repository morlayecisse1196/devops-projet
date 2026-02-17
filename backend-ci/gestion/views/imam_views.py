from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from gestion.models.imam import Imam
from gestion.serializers.imam_serializer import (
    ImamSerializer,
    SaveImamSerializer,
    UpdateImamSerializer
)
from gestion.services.imam_service import ImamService


class ImamAPIView(generics.GenericAPIView):
    """GET tous les imams, POST créer un imam"""
    permission_classes = [IsAuthenticated]
    queryset = Imam.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveImamSerializer
        return ImamSerializer

    def get(self, request):
        imams = ImamService.get_all()
        serializer = ImamSerializer(imams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        imam = ImamService.create(serializer.validated_data)
        return Response(
            {"message": "Imam créé avec succès", "id": imam.id},
            status=status.HTTP_201_CREATED
        )


class ImamDetailAPIView(generics.GenericAPIView):
    """GET by id, PUT, DELETE"""
    permission_classes = [IsAuthenticated]
    queryset = Imam.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateImamSerializer
        return ImamSerializer

    def get(self, request, id):
        imam = ImamService.get_by_id(id)
        serializer = ImamSerializer(imam)
        return Response(serializer.data)

    def put(self, request, id):
        imam = ImamService.get_by_id(id)
        serializer = self.get_serializer(imam, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        imam = ImamService.update(imam, serializer.validated_data)
        return Response(ImamSerializer(imam).data)

    def delete(self, request, id):
        imam = ImamService.get_by_id(id)
        ImamService.delete(imam)
        return Response(status=status.HTTP_204_NO_CONTENT)
