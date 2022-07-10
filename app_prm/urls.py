from django.urls import path
from app_prm import brand_partner, end_user

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('plans',brand_partner.PlanFormViewSet,basename='plans')
router.register('promotions',brand_partner.PromotionFormViewSet,basename='promotions')
router.register('customer-goals',end_user.CustomerGoalsFormViewSet,basename='customer-goals')
router.register('available-plans',end_user.AvailablePlansViewSet,basename='available-plans')
router.register('active-promotions',end_user.ActivePromotionsViewSet,basename='active-promotions')

urlpatterns = [

]+ router.urls