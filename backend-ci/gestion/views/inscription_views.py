from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from gestion.models.inscription import Inscription
from gestion.serializers.inscription_serializer import (
    InscriptionSerializer,
    SaveInscriptionSerializer,
    UpdateInscriptionSerializer
)
from gestion.services.inscription_service import InscriptionService


class InscriptionAPIView(generics.GenericAPIView):
    """GET toutes les inscriptions, POST créer une inscription"""
    permission_classes = [IsAuthenticated]
    queryset = Inscription.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveInscriptionSerializer
        return InscriptionSerializer

    def get(self, request):
        inscriptions = InscriptionService.get_all()
        serializer = InscriptionSerializer(inscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            inscription = InscriptionService.create(serializer.validated_data)
            return Response(
                {"message": "Inscription créée avec succès", "id": inscription.id},
                status=status.HTTP_201_CREATED
            )
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class InscriptionDetailAPIView(generics.GenericAPIView):
    """GET by id, PUT, DELETE"""
    permission_classes = [IsAuthenticated]
    queryset = Inscription.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateInscriptionSerializer
        return InscriptionSerializer

    def get(self, request, id):
        inscription = InscriptionService.get_by_id(id)
        serializer = InscriptionSerializer(inscription)
        return Response(serializer.data)

    def put(self, request, id):
        inscription = InscriptionService.get_by_id(id)
        serializer = self.get_serializer(inscription, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        inscription = InscriptionService.update(inscription, serializer.validated_data)
        return Response(InscriptionSerializer(inscription).data)

    def delete(self, request, id):
        inscription = InscriptionService.get_by_id(id)
        InscriptionService.delete(inscription)
        return Response(status=status.HTTP_204_NO_CONTENT)
