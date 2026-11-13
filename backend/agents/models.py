from django.db import models

class AgentWallet(models.Model):
    name = models.CharField(max_length=100)
    xrpl_address = models.CharField(max_length=35, unique=True)
    seed = models.CharField(max_length=100)  # store securely in production!

class Mandate(models.Model):
    agent_wallet = models.ForeignKey(AgentWallet, on_delete=models.CASCADE, related_name="mandates")
    max_spend_amount = models.DecimalField(max_digits=20, decimal_places=6)  # max amount per transaction
    allowed_recipients = models.JSONField(default=list)  # list of approved XRPL addresses
    active = models.BooleanField(default=True)
