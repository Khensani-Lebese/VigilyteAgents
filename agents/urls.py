from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentWalletViewSet, MandateViewSet

router = DefaultRouter()
router.register(r'wallets', AgentWalletViewSet)
router.register(r'mandates', MandateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
