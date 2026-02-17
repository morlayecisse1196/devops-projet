from django.urls import path
from gestion.views.inscription_views import InscriptionAPIView, InscriptionDetailAPIView

urlpatterns = [
    path('inscriptions/', InscriptionAPIView.as_view(), name='inscription-list'),
    path('inscriptions/<int:id>/', InscriptionDetailAPIView.as_view(), name='inscription-detail'),
]
