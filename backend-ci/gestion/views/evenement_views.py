from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from gestion.models.evenement import Evenement
from gestion.serializers.evenement_serializer import (
    EvenementSerializer,
    SaveEvenementSerializer,
    UpdateEvenementSerializer
)
from gestion.services.evenement_service import EvenementService


class EvenementAPIView(generics.GenericAPIView):
    """GET tous les événements, POST créer un événement"""
    permission_classes = [IsAuthenticated]
    queryset = Evenement.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveEvenementSerializer
        return EvenementSerializer

    def get(self, request):
        evenements = EvenementService.get_all()
        serializer = EvenementSerializer(evenements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        evenement = EvenementService.create(serializer.validated_data)
        return Response(
            {"message": "Événement créé avec succès", "id": evenement.id},
            status=status.HTTP_201_CREATED
        )


class EvenementDetailAPIView(generics.GenericAPIView):
    """GET by id, PUT, DELETE"""
    permission_classes = [IsAuthenticated]
    queryset = Evenement.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateEvenementSerializer
        return EvenementSerializer

    def get(self, request, id):
        evenement = EvenementService.get_by_id(id)
        serializer = EvenementSerializer(evenement)
        return Response(serializer.data)

    def put(self, request, id):
        evenement = EvenementService.get_by_id(id)
        serializer = self.get_serializer(evenement, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        evenement = EvenementService.update(evenement, serializer.validated_data)
        return Response(EvenementSerializer(evenement).data)

    def delete(self, request, id):
        evenement = EvenementService.get_by_id(id)
        EvenementService.delete(evenement)
        return Response(status=status.HTTP_204_NO_CONTENT)
