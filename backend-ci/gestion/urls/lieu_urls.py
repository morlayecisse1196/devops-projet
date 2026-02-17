from django.urls import path
from gestion.views.lieu_views import LieuAPIView, LieuDetailAPIView

urlpatterns = [
    path('lieux/', LieuAPIView.as_view(), name='lieu-list'),
    path('lieux/<int:id>/', LieuDetailAPIView.as_view(), name='lieu-detail'),
]
