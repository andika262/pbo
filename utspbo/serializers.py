from rest_framework import serializers
from app_utspbo.models import koor

class koorSerialzer(serializers.ModelSerializer):
    class Meta:
        model = koor
        fields = '__all__'