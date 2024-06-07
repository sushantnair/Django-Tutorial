from rest_framework import generics #type: ignore
from .models import BioData
from .serializers import BioDataSerializer

# Create your views here.
class BioDataListCreate(generics.ListCreateAPIView):
    queryset = BioData.objects.all()
    serializer_class = BioDataSerializer
    
