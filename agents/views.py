from rest_framework import viewsets
from .models import AgentWallet, Mandate
from .serializers import AgentWalletSerializer, MandateSerializer

class AgentWalletViewSet(viewsets.ModelViewSet):
    queryset = AgentWallet.objects.all()
    serializer_class = AgentWalletSerializer

class MandateViewSet(viewsets.ModelViewSet):
    queryset = Mandate.objects.all()
    serializer_class = MandateSerializer
