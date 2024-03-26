from django.shortcuts import render
from ..models import ExternalStakeholder
from .serializers import FormDataSerializer
from rest_framework import generics
# Create your views here.
class ExternalStakeholdersList(generics.ListCreateAPIView):
    queryset = ExternalStakeholder.objects.all()
    serializer_class=FormDataSerializer

class ExternalStakeholderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExternalStakeholder.objects.all()
    serializer_class=FormDataSerializer