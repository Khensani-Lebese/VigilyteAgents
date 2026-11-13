from rest_framework import serializers
from .models import AgentWallet, Mandate

class AgentWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentWallet
        fields = "__all__"

class MandateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandate
        fields = "__all__"
