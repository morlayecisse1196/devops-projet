from django.urls import path
from gestion.views.imam_views import ImamAPIView, ImamDetailAPIView

urlpatterns = [
    path('imams/', ImamAPIView.as_view(), name='imam-list'),
    path('imams/<int:id>/', ImamDetailAPIView.as_view(), name='imam-detail'),
]
