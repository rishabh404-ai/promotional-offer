from operator import mod
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from app_prm.choices import *
from django.contrib.auth.models import User

# Create your models here

class Plan(models.Model):
    plan_name= models.CharField(
        max_length=200
    )
    amount_options= models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Plan should be of atleast Rs 1/-"
    )
    tenure_options= models.CharField(
        max_length=8, 
        choices=TENURE_CHOICES
    )
    benefit_percentage = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    benefit_type= models.CharField(
        max_length=12, 
        choices=BENEFIT_CHOICES
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    is_active = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return self.plan_name

class Promotion(models.Model):
    promo_name = models.CharField(
        max_length=200
    )
    promo_type = models.CharField(
        max_length=23, 
        choices=PROMO_CHOICES
    )
    plan = models.ForeignKey(
        to=Plan,
        on_delete=models.PROTECT
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    promo_start = models.DateField(
        null=True,
        blank=True
    )
    promo_end = models.DateField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )    
    is_active = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return self.promo_name
    

class CustomerGoals(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    enrolled_plan = models.ForeignKey(
        to=Plan,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    selected_promo = models.ForeignKey(
        to=Promotion,
        on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )    
    cashback_amount = models.FloatField(
        null=True,
        blank=True,
        help_text='Total Cashback Amount Based On Benefit Percentage Of Plan'
    )
    is_payment_recieved = models.BooleanField(
        default=False,
    )
    is_customer_plan_active = models.BooleanField(
        default=False,
    )




