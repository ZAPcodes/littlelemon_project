from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import MenuItem, BookingTable
from .serializers import MenuSerializer, BookingTableSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer

def index(request):
    return render(request, 'index.html')
