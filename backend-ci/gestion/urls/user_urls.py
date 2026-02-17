from django.urls import path
from gestion.views.user_views import UserAPIView, UserDetailAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetailAPIView.as_view(), name='user-detail'),
]
