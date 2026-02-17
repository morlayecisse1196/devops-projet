from django.http import JsonResponse
from django.db import connection


def health_check(request):
    """Endpoint de health check pour Docker"""
    try:
        # Tester la connexion à la base de données
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        return JsonResponse({
            "status": "healthy",
            "database": "connected"
        })
    except Exception as e:
        return JsonResponse({
            "status": "unhealthy",
            "error": str(e)
        }, status=503)
