from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from gestion.models.notification import Notification
from gestion.serializers.notification_serializer import (
    NotificationSerializer,
    SaveNotificationSerializer,
    UpdateNotificationSerializer
)
from gestion.services.notification_service import NotificationService


class NotificationAPIView(generics.GenericAPIView):
    """GET toutes les notifications, POST créer une notification"""
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveNotificationSerializer
        return NotificationSerializer

    def get(self, request):
        notifications = NotificationService.get_all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = NotificationService.create(serializer.validated_data)
        return Response(
            {"message": "Notification créée avec succès", "id": notification.id},
            status=status.HTTP_201_CREATED
        )


class NotificationDetailAPIView(generics.GenericAPIView):
    """GET by id, PUT, DELETE"""
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateNotificationSerializer
        return NotificationSerializer

    def get(self, request, id):
        notification = NotificationService.get_by_id(id)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

    def put(self, request, id):
        notification = NotificationService.get_by_id(id)
        serializer = self.get_serializer(notification, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        notification = NotificationService.update(notification, serializer.validated_data)
        return Response(NotificationSerializer(notification).data)

    def delete(self, request, id):
        notification = NotificationService.get_by_id(id)
        NotificationService.delete(notification)
        return Response(status=status.HTTP_204_NO_CONTENT)
