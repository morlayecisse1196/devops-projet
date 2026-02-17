from django.urls import path, include

urlpatterns = [
    path('', include('gestion.urls.user_urls')),
    path('', include('gestion.urls.lieu_urls')),
    path('', include('gestion.urls.evenement_urls')),
    path('', include('gestion.urls.inscription_urls')),
    path('', include('gestion.urls.imam_urls')),
    path('', include('gestion.urls.histoire_urls')),
    path('', include('gestion.urls.notification_urls')),
    path('', include('gestion.urls.notification_user_urls')),
]
