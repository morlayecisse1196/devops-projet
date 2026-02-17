from django.urls import path
from gestion.views.notification_user_views import NotificationUserAPIView, NotificationUserDetailAPIView

urlpatterns = [
    path('notification-users/', NotificationUserAPIView.as_view(), name='notification-user-list'),
    path('notification-users/<int:id>/', NotificationUserDetailAPIView.as_view(), name='notification-user-detail'),
]
