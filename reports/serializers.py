from rest_framework import serializers
from .models import FireReport

class FireReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireReport
        fields = '__all__'
