from django.shortcuts import render

# Create your views here.
import csv
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import FireReport
from .serializers import FireReportSerializer
from django.shortcuts import render

def map_view(request):
    return render(request, 'reports/map.html')

class FireReportViewSet(viewsets.ModelViewSet):
    queryset = FireReport.objects.all()
    serializer_class = FireReportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the report
        serializer.save(user=self.request.user)

def nasa_fire_data_view(request):
    file_path = 'static/nasa_fire_data.csv'
    fire_data = []

    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                fire_data.append({
                    'latitude': float(row['latitude']),
                    'longitude': float(row['longitude']),
                    'brightness': float(row['brightness']),
                    'confidence': row['confidence'],
                })
    except FileNotFoundError:
        return JsonResponse({'error': 'NASA fire data not available'}, status=404)

    return JsonResponse(fire_data, safe=False)
