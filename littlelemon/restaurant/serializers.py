from rest_framework.serializers import ModelSerializer
from .models import *

class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

class BookingTableSerializer(ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'

