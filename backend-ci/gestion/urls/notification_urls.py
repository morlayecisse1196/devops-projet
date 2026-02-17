from django.urls import path
from gestion.views.notification_views import NotificationAPIView, NotificationDetailAPIView

urlpatterns = [
    path('notifications/', NotificationAPIView.as_view(), name='notification-list'),
    path('notifications/<int:id>/', NotificationDetailAPIView.as_view(), name='notification-detail'),
]
