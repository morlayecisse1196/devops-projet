from .user_views import UserAPIView, UserDetailAPIView
from .lieu_views import LieuAPIView, LieuDetailAPIView
from .evenement_views import EvenementAPIView, EvenementDetailAPIView
from .inscription_views import InscriptionAPIView, InscriptionDetailAPIView
from .imam_views import ImamAPIView, ImamDetailAPIView
from .histoire_views import HistoireAPIView, HistoireDetailAPIView
from .notification_views import NotificationAPIView, NotificationDetailAPIView
from .notification_user_views import NotificationUserAPIView, NotificationUserDetailAPIView

__all__ = [
    'UserAPIView', 'UserDetailAPIView',
    'LieuAPIView', 'LieuDetailAPIView',
    'EvenementAPIView', 'EvenementDetailAPIView',
    'InscriptionAPIView', 'InscriptionDetailAPIView',
    'ImamAPIView', 'ImamDetailAPIView',
    'HistoireAPIView', 'HistoireDetailAPIView',
    'NotificationAPIView', 'NotificationDetailAPIView',
    'NotificationUserAPIView', 'NotificationUserDetailAPIView',
]
