from django.urls import path
from gestion.views.histoire_views import HistoireAPIView, HistoireDetailAPIView

urlpatterns = [
    path('histoires/', HistoireAPIView.as_view(), name='histoire-list'),
    path('histoires/<int:id>/', HistoireDetailAPIView.as_view(), name='histoire-detail'),
]
