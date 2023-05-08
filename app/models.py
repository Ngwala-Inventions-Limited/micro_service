from django.db import models

# Create your models here.

class Transaction(models.Model):
    uid = models.CharField(max_length=10, null=True)
    amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, null=True)
    register = models.BooleanField(null=True)
    version = models.PositiveIntegerField(default=0, null=True)
    
    def __str__(self):
        return self.uid