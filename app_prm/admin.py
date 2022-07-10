from django.contrib import admin
from app_prm.models import *

# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display  = ('id','plan_name','amount_options','tenure_options','benefit_percentage','benefit_type','created_at','updated_at',
                    'is_active')

    list_filter   =  ('id','plan_name','amount_options','tenure_options','benefit_percentage','benefit_type',
                    'is_active')

    search_fields =  ('id','plan_name','amount_options','tenure_options','benefit_percentage','benefit_type',
                    'is_active')

    ordering      = ('-amount_options',)
admin.site.register(Plan, PlanAdmin)

class PromotionAdmin(admin.ModelAdmin):
    list_display  = ('id','promo_start','promo_end','promo_name','promo_type','plan','description','created_at','updated_at',
                    'is_active')

    list_filter   =  ('id','promo_name','promo_type','promo_start','promo_end',
                    'is_active')

    search_fields =  ('id','promo_name','promo_type','promo_start','promo_end',
                    'is_active')

    ordering      = ('-promo_start',)
admin.site.register(Promotion, PromotionAdmin)

class CustomerGoalsAdmin(admin.ModelAdmin):
    list_display  = ('id','user','enrolled_plan','selected_promo','cashback_amount','is_payment_recieved',
                    'is_customer_plan_active','created_at','updated_at')

    list_filter   =  ('id','is_payment_recieved','is_customer_plan_active')

    search_fields =  ('id','is_payment_recieved','is_customer_plan_active')

    ordering      = ('-id',)
admin.site.register(CustomerGoals, CustomerGoalsAdmin)
