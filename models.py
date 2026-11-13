from django.db import models

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('dispatched', 'Dispatched'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('payment_ready', 'Payment Ready'),
    ]

    reference = models.CharField(max_length=30, unique=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='dispatched')
    dispatched_date = models.DateField(null=True, blank=True)
    in_transit_date = models.DateField(null=True, blank=True)
    delivered_date = models.DateField(null=True, blank=True)
    payment_ready_date = models.DateField(null=True, blank=True)
    carrier = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    agreement_type = models.CharField(max_length=50)

    def __str__(self):
        return self.reference

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('released', 'Released'),
        ('failed', 'Failed'),
    ]
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    transaction_hash = models.CharField(max_length=100, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.shipment.reference} - {self.amount} - {self.status}"

class DeliveryEvidence(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='evidences')
    file = models.FileField(upload_to='delivery_evidence/')
    verified = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evidence for {self.shipment.reference}"

class ActivityLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp}: {self.description[:50]}"

class AIRecommendation(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name='recommendations')
    recommendation_text = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Rec for {self.shipment.reference} - {self.status}"

