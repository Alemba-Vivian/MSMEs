from rest_framework import serializers
from msme_app.models import MSMEquestionnaire

class MSMEquestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = MSMEquestionnaire
        fields = '__all__'
