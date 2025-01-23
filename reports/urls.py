from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FireReportViewSet, map_view

# Create a router for the FireReport API
router = DefaultRouter()
router.register(r'fire-reports', FireReportViewSet)

# Define the app's URL patterns
urlpatterns = [
    # Include the API routes from the router
    path('', include(router.urls)),

    # Route for the map view
    path('map/', map_view, name='map'),
]