from app_prm.serializers import *
from app_prm.models import * 
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action


class CustomerGoalsFormViewSet(viewsets.ModelViewSet):  
    '''
    API Endpoint to enroll in a plan by end-user
    '''

    serializer_class = CustomerGoalsSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomerGoals.objects.filter(user=self.request.user.id).order_by('-id')

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)    
        payment = (serializer.data)['is_payment_recieved']
        object_id = (serializer.data)['id']
        selected_plan = int((serializer.data)['selected_promo']['plan']['id'])
        plan_id = Plan.objects.get(pk=selected_plan)
        if payment == True:
            benefit_percentage = (serializer.data)['selected_promo']['plan']['benefit_percentage']
            plan_amount = (serializer.data)['selected_promo']['plan']['amount_options']
            cashback_amount = (plan_amount * benefit_percentage)/100
            update_customer_plan_status_and_cashback_amount = CustomerGoals.objects.filter(
                user=self.request.user, pk=object_id).update(
                    cashback_amount=cashback_amount, is_customer_plan_active=True, enrolled_plan=plan_id)
            return Response(
                    {
                      'status' : 'success',
                      'message': 'Payment recieved ! Plan has been purchased successfully.',
                }, status=status.HTTP_201_CREATED)          
        
        else:
            update_customer_plan_status_and_cashback_amount = CustomerGoals.objects.filter(
                user=self.request.user, pk=object_id).update(
                    cashback_amount=None, is_customer_plan_active=False, enrolled_plan=plan_id)
            return Response(
                    {
                      'status' : 'failed',
                      'message': 'Payment not completed. Please try again !',
                }, status=status.HTTP_400_BAD_REQUEST)          
        
    def perform_create(self,serializer):
        serializer.save(user=self.request.user) 
    
    @action(methods=['get'],detail=False) 
    def customer_active_plans(self,request):
        '''
        This filter shows all the transactions of plans of users which 
        got success with their payments and hence purchased the plans.
        '''

        queryset = CustomerGoals.objects.filter(user=self.request.user.id, is_customer_plan_active=True).order_by('-id')
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)      

    @action(methods=['get'],detail=False) 
    def customer_failed_transactions(self,request):
        '''
        This filter shows all the transactions of plans of users which 
        got failed due to payment failure.
        '''

        queryset = CustomerGoals.objects.filter(user=self.request.user.id, is_customer_plan_active=False).order_by('-id')
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
        

class AvailablePlansViewSet(viewsets.ReadOnlyModelViewSet):  
    '''
    API Endpoint to display list of all available plans to end-user
    '''

    queryset=  Plan.objects.all()
    serializer_class = PlansSerializer 

class ActivePromotionsViewSet(viewsets.ReadOnlyModelViewSet):  
    '''
    API Endpoint to display list of all active promotions to end-user
    Users can also filter the promotions based on promo_name and/or promo_type
    '''

    serializer_class = PromotionsSerializer 

    def get_queryset(self):
        promo_name= self.request.query_params.get('promo_name')
        promo_type= self.request.query_params.get('promo_type')

        if promo_name and promo_type: 
            queryset = Promotion.objects.filter(promo_name=promo_name,promo_type=promo_type).order_by('-id')
        elif promo_type:
            queryset = Promotion.objects.filter(promo_type=promo_type).order_by('-id')
        elif promo_name:   
            queryset = Promotion.objects.filter(promo_name=promo_name).order_by('-id')
        else:
            queryset = Promotion.objects.all().order_by('-id')

        return queryset    