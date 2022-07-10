from rest_framework import serializers
from app_prm.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_active']

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class PromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['plan'] =  PlansSerializer(read_only=True)
        return super(PromotionsSerializer, self).to_representation(instance)

class CustomerGoalsSerializer(serializers.ModelSerializer):
    
    cashback_amount = serializers.ReadOnlyField()
    user = UserSerializer(read_only=True)
    is_customer_plan_active = serializers.ReadOnlyField()
    enrolled_plan =  serializers.ReadOnlyField()

    class Meta:
        model = CustomerGoals
        fields = ['id','user','enrolled_plan','selected_promo','cashback_amount','is_payment_recieved','is_customer_plan_active']      

    def to_representation(self, instance):
        self.fields['enrolled_plan'] =  PlansSerializer(read_only=True)
        self.fields['selected_promo'] = PromotionsSerializer(read_only=True)
        return super(CustomerGoalsSerializer, self).to_representation(instance)
    
