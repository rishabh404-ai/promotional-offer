from app_prm.serializers import *
from app_prm.models import * 
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class PlanFormViewSet(viewsets.ModelViewSet):  
    '''
    API Endpoint to create a plan
    '''

    queryset=  Plan.objects.all().order_by('-id')
    serializer_class = PlansSerializer   

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)    
        return Response(
                    {
                      'status' : 'success',
                      'message': 'Plan created succesfully',
                      'data': serializer.data
                }, status=status.HTTP_201_CREATED)          
        
    def perform_create(self,serializer):
        serializer.save() 
    
class PromotionFormViewSet(viewsets.ModelViewSet):  
    '''
    API Endpoint to create a promotion for an existing plan
    '''

    queryset=  Promotion.objects.all().order_by('-id')
    serializer_class = PromotionsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)    
        return Response(
                    {
                      'status' : 'success',
                      'message': 'Promotion created succesfully',
                      'data': serializer.data
                }, status=status.HTTP_201_CREATED)          
        
    def perform_create(self,serializer):
        serializer.save() 