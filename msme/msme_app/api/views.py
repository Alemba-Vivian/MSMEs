
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, mixins, generics
from rest_framework import viewsets

from msme_app.api.serializers import MSMEquestionnaireSerializer
from msme_app.models import MSMEquestionnaire

# class formcr(generics.ListCreateAPIView):
#     queryset = MSMEquestionnaire.objects.all()
#     serializer_class=MSMEquestionnaireSerializer
    
# class formrud(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MSMEquestionnaire.objects.all()
#     serializer_class=MSMEquestionnaireSerializer


class formViewSet(viewsets.ViewSet):
    @action(detail=False,methods=['GET'])

    
    def list(self, request):
        queryset = MSMEquestionnaire.objects.all()
        serializer = MSMEquestionnaireSerializer(queryset, many=True)
        return Response(serializer.data)
        
    # def retrieve(self, request, pk=None):
    #     queryset=MSMEquestionnaire.objects.all()
    #     user_response=get_object_or_404(queryset, pk=pk)
    #     serializer = MSMEquestionnaireSerializer( user_response)
    #     return Response(serializer.data)
    
    @action(detail=False,methods=['POST'])
    def create(self, request):
        uresponse=request.data
        serializer = MSMEquestionnaireSerializer(data=request.data)
        if serializer.is_valid():
                                    
            # name =uresponse['name']
            # phone =uresponse['phone']
            # email = uresponse['email']
            # subcounty=uresponse['subcounty']
            # ward=uresponse['ward']
            # disability=uresponse['disability']
            # cboreg=uresponse['cboreg']
            # groupname=uresponse['groupname']
            # position=uresponse['position']
            # groupreg=uresponse['groupreg']
            # groupoperationalyears=uresponse['groupoperationalyears']
            
            name =uresponse['name']
            phone =uresponse['phone']
            email = uresponse['email']
            subCounty=uresponse['subCounty']
            ward=uresponse['ward']
            disability=uresponse['disability']
            chama=uresponse['chama']
            nameOfChama=uresponse['nameOfChama']
            membershipPosition=uresponse['membershipPosition']
            isChamaRegistered=uresponse['isChamaRegistered']
            chamaOperation=uresponse['chamaOperation']
            
            msmse_questionnaire=MSMEquestionnaire.objects.create(name= name,
            # phone =phone,
            # email = email,
            # subcounty=subcounty,
            # ward=ward,
            # disability=disability,
            # cboreg=cboreg,
            # groupname=groupname,
            # position=position,
            # groupreg=groupreg,      
            # groupoperationalyears=groupoperationalyears)
            
            phone =phone,
            email = email,
            subCounty= subCounty,
            ward=ward,
            chama=chama,
            disability=disability,
           nameOfChama=nameOfChama,
           membershipPosition= membershipPosition,
           isChamaRegistered= isChamaRegistered,      
           chamaOperation=chamaOperation)
            serializer=MSMEquestionnaireSerializer(msmse_questionnaire)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        else:
            return Response(serializer.errors)
        
class formDetailViewSet(viewsets.ViewSet):
    @action(detail=True,methods=['GET'])
    def retrieve(self, request, pk):
        try:
            user_response=MSMEquestionnaire.objects.get(pk=pk)
        except MSMEquestionnaire.DoesNotExist:
            return Response({'Error': 'Platform not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=MSMEquestionnaireSerializer(user_response)
        return Response(serializer.data)
    
    @action(detail=True,methods=['PUT'])
    def update(self, request, pk):
        user_response=MSMEquestionnaire.objects.get(pk=pk)
        serializer=MSMEquestionnaireSerializer(user_response, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True,methods=['DELETE'])
    def destroy(self, request, pk):
        user_response=MSMEquestionnaire.objects.get(pk=pk)
        user_response.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    