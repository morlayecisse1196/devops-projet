from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from gestion.models.lieu import Lieu
from gestion.serializers.lieu_serializer import (
    LieuSerializer,
    SaveLieuSerializer,
    UpdateLieuSerializer
)
from gestion.services.lieu_service import LieuService


class LieuAPIView(generics.GenericAPIView):
    """GET tous les lieux, POST créer un lieu"""
    permission_classes = [IsAuthenticated]
    queryset = Lieu.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveLieuSerializer
        return LieuSerializer

    def get(self, request):
        lieux = LieuService.get_all()
        serializer = LieuSerializer(lieux, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lieu = LieuService.create(serializer.validated_data)
        return Response(
            {"message": "Lieu créé avec succès", "id": lieu.id},
            status=status.HTTP_201_CREATED
        )


class LieuDetailAPIView(generics.GenericAPIView):
    """GET by id, PUT, DELETE"""
    permission_classes = [IsAuthenticated]
    queryset = Lieu.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateLieuSerializer
        return LieuSerializer

    def get(self, request, id):
        lieu = LieuService.get_by_id(id)
        serializer = LieuSerializer(lieu)
        return Response(serializer.data)

    def put(self, request, id):
        lieu = LieuService.get_by_id(id)
        serializer = self.get_serializer(lieu, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        lieu = LieuService.update(lieu, serializer.validated_data)
        return Response(LieuSerializer(lieu).data)

    def delete(self, request, id):
        lieu = LieuService.get_by_id(id)
        LieuService.delete(lieu)
        return Response(status=status.HTTP_204_NO_CONTENT)
