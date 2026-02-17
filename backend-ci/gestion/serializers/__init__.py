from .user_serializer import UserSerializer, SaveUserSerializer, UpdateUserSerializer
from .lieu_serializer import LieuSerializer, SaveLieuSerializer, UpdateLieuSerializer
from .evenement_serializer import EvenementSerializer, SaveEvenementSerializer, UpdateEvenementSerializer
from .inscription_serializer import InscriptionSerializer, SaveInscriptionSerializer, UpdateInscriptionSerializer
from .imam_serializer import ImamSerializer, SaveImamSerializer, UpdateImamSerializer
from .histoire_serializer import HistoireSerializer, SaveHistoireSerializer, UpdateHistoireSerializer
from .notification_serializer import NotificationSerializer, SaveNotificationSerializer, UpdateNotificationSerializer
from .notification_user_serializer import NotificationUserSerializer, SaveNotificationUserSerializer, UpdateNotificationUserSerializer

__all__ = [
    # User
    'UserSerializer', 'SaveUserSerializer', 'UpdateUserSerializer',
    # Lieu
    'LieuSerializer', 'SaveLieuSerializer', 'UpdateLieuSerializer',
    # Evenement
    'EvenementSerializer', 'SaveEvenementSerializer', 'UpdateEvenementSerializer',
    # Inscription
    'InscriptionSerializer', 'SaveInscriptionSerializer', 'UpdateInscriptionSerializer',
    # Imam
    'ImamSerializer', 'SaveImamSerializer', 'UpdateImamSerializer',
    # Histoire
    'HistoireSerializer', 'SaveHistoireSerializer', 'UpdateHistoireSerializer',
    # Notification
    'NotificationSerializer', 'SaveNotificationSerializer', 'UpdateNotificationSerializer',
    # NotificationUser
    'NotificationUserSerializer', 'SaveNotificationUserSerializer', 'UpdateNotificationUserSerializer',
]
