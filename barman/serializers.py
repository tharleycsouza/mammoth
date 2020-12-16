from rest_framework.serializers import ModelSerializer
from barman.models import Diagnose
from rest_framework.serializers import ModelSerializer


class DiagnoseSerializer(ModelSerializer):

    class Meta:
        model = Diagnose
        fields = '__all__'
