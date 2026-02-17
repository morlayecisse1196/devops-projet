from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from gestion.models.notification_user import NotificationUser
from gestion.serializers.notification_user_serializer import (
    NotificationUserSerializer,
    SaveNotificationUserSerializer,
    UpdateNotificationUserSerializer
)
from gestion.services.notification_user_service import NotificationUserService


class NotificationUserAPIView(generics.GenericAPIView):
    """GET toutes les notifications utilisateur, POST créer une notification utilisateur"""
    permission_classes = [IsAuthenticated]
    queryset = NotificationUser.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveNotificationUserSerializer
        return NotificationUserSerializer

    def get(self, request):
        notification_users = NotificationUserService.get_all()
        serializer = NotificationUserSerializer(notification_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification_user = NotificationUserService.create(serializer.validated_data)
        return Response(
            {"message": "Notification utilisateur créée avec succès", "id": notification_user.id},
            status=status.HTTP_201_CREATED
        )


class NotificationUserDetailAPIView(generics.GenericAPIView):
    """GET by id, PUT, DELETE"""
    permission_classes = [IsAuthenticated]
    queryset = NotificationUser.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateNotificationUserSerializer
        return NotificationUserSerializer

    def get(self, request, id):
        notification_user = NotificationUserService.get_by_id(id)
        serializer = NotificationUserSerializer(notification_user)
        return Response(serializer.data)

    def put(self, request, id):
        notification_user = NotificationUserService.get_by_id(id)
        serializer = self.get_serializer(notification_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        notification_user = NotificationUserService.update(notification_user, serializer.validated_data)
        return Response(NotificationUserSerializer(notification_user).data)

    def delete(self, request, id):
        notification_user = NotificationUserService.get_by_id(id)
        NotificationUserService.delete(notification_user)
        return Response(status=status.HTTP_204_NO_CONTENT)
