from rest_framework import serializers
from .models import AgentWallet, Mandate

class AgentWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentWallet
        fields = "__all__"
        extra_kwargs = {
            "seed": {"write_only": True},
        }

class MandateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandate
        fields = "__all__"
