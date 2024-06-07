from rest_framework import serializers #type: ignore
from .models import BioData

class BioDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioData
        fields = '__all__'