from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from gestion.models.user import User
from gestion.serializers.user_serializer import (
    UserSerializer,
    SaveUserSerializer,
    UpdateUserSerializer
)
from gestion.services.user_service import UserService


class UserAPIView(generics.GenericAPIView):
    """GET tous les users, POST créer un user"""
    queryset = User.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SaveUserSerializer
        return UserSerializer

    def get(self, request):
        users = UserService.get_all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.create(serializer.validated_data)
        return Response(
            {"message": "Utilisateur créé avec succès", "id": user.id},
            status=status.HTTP_201_CREATED
        )


class UserDetailAPIView(generics.GenericAPIView):
    """GET by id, PUT, DELETE"""
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateUserSerializer
        return UserSerializer

    def get(self, request, id):
        user = UserService.get_by_id(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = UserService.get_by_id(id)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = UserService.update(user, serializer.validated_data)
        return Response(UserSerializer(user).data)

    def delete(self, request, id):
        user = UserService.get_by_id(id)
        UserService.delete(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
