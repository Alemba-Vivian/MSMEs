from django.shortcuts import render
from ..models import ExternalStakeholder
from .serializers import FormDataSerializer
# from rest_framework import generics
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.
# class ExternalStakeholdersList(generics.ListCreateAPIView):
#     queryset = ExternalStakeholder.objects.all()
#     serializer_class=FormDataSerializer

# class ExternalStakeholderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ExternalStakeholder.objects.all()
#     serializer_class=FormDataSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class ExternalStakeholdersViewSet(viewsets.ViewSet):
    
    @action(detail=False,methods=['GET'])
    def list(self, request):
            queryset = ExternalStakeholder.objects.all()
            serializer = FormDataSerializer(queryset, many=True)
            return Response(serializer.data)
    @action(detail=False,methods=['POST'])
    def create(self, request):
        if request.method == 'POST':
            
           
            payload=request.data
            serializer = FormDataSerializer(data=request.data)
        
            if serializer.is_valid():
                name = payload['name']
                phone_number = payload['phone_number']
                email = payload['email']
                sub_county = payload['sub_county']
                ward = payload['ward']
                member_of_group = payload['member_of_group']
                group_name = payload['group_name']
                membership_position = payload['membership_position']
                group_registered = payload['group_registered']
                group_operational_years = payload['group_operational_years']
                
                external_stakeholder = ExternalStakeholder.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                sub_county=sub_county,
                ward=ward,
                member_of_group=member_of_group,
                group_name=group_name,
                membership_position=membership_position,
                group_registered=group_registered,
                group_operational_years=group_operational_years
            )
                serializer=FormDataSerializer(external_stakeholder)
              
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExStakeholdersDetailViewSet(viewsets.ViewSet):
    @action(detail=True,methods=['GET'])
    def retrieve(self, request, pk=None):
        
        try:
            stakeholder = ExternalStakeholder.objects.get(pk=pk)
        except ExternalStakeholder.DoesNotExist:
            return Response({"message": "stakeholder details not foud"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FormDataSerializer(stakeholder)
        return Response(serializer.data)
    @action(detail=True,methods=['PUT'])
    def update(self, request, pk=None):
        try:
            stakeholder = ExternalStakeholder.objects.get(pk=pk)
        except ExternalStakeholder.DoesNotExist:
            return Response({"message": "Stakeholder details not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FormDataSerializer(stakeholder, data=request.data)
        if serializer.is_valid():
            # Assuming all fields are required
            stakeholder.name = serializer.validated_data['name']
            stakeholder.phone_number = serializer.validated_data['phone_number']
            stakeholder.email = serializer.validated_data['email']
            stakeholder.sub_county = serializer.validated_data['sub_county']
            stakeholder.ward = serializer.validated_data['ward']
            stakeholder.member_of_group = serializer.validated_data['member_of_group']
            stakeholder.group_name = serializer.validated_data['group_name']
            stakeholder.membership_position = serializer.validated_data['membership_position']
            stakeholder.group_registered = serializer.validated_data['group_registered']
            stakeholder.group_operational_years = serializer.validated_data['group_operational_years']
            stakeholder.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    @action(detail=True,methods=['DELETE'])
       
    def destroy(self, request, pk=None):
        try:
            stakeholder = ExternalStakeholder.objects.get(pk=pk)
        except ExternalStakeholder.DoesNotExist:
            return Response({"message": "stakeholder details not foud"}, status=status.HTTP_404_NOT_FOUND)
        
      
        stakeholder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
