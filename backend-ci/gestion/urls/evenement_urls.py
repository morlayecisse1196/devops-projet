from django.urls import path
from gestion.views.evenement_views import EvenementAPIView, EvenementDetailAPIView

urlpatterns = [
    path('evenements/', EvenementAPIView.as_view(), name='evenement-list'),
    path('evenements/<int:id>/', EvenementDetailAPIView.as_view(), name='evenement-detail'),
]
