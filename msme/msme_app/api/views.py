
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from msme_app.api.serializers import MSMEquestionnaireSerializer
from msme_app.models import MSMEquestionnaire

class formcr(generics.ListCreateAPIView):
    queryset = MSMEquestionnaire.objects.all()
    serializer_class=MSMEquestionnaireSerializer
    
class formrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = MSMEquestionnaire.objects.all()
    serializer_class=MSMEquestionnaireSerializer
