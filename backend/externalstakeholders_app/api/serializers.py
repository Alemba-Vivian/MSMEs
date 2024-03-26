from rest_framework import serializers
from ..models import ExternalStakeholder

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalStakeholder
        fields = '__all__'
