from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DigitalItemSerializer, PhysicalItemSerializer
from .models import digital_item,SalePage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
class DigitalItemViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    serializer_class = DigitalItemSerializer
    queryset = digital_item.objects.all()

    def perform_create(self, serializer):
        serializer.save(SalePage = SalePage.objects.get(pk='1'))



@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'books': reverse('book-list',request=request,format=None),
        #'chapters': reverse('chapter-list',request=request,format=None),
        #'authors': reverse('author-list',request=request,format=None)
    })