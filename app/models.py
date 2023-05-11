from django.db import models
from django.utils import timezone

# Create your models here.

class Transaction(models.Model):
    uid = models.CharField(max_length=10, null=True)
    amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    date_trans = models.DateTimeField(null=True, blank= True, help_text="Date of last Transaction", verbose_name="Last Transaction")
    register = models.BooleanField(null=True)
    version = models.PositiveIntegerField(default=1, null=True, help_text="Do not touch this field")
    old_version = models.PositiveIntegerField(default=0, null=True, help_text="Do not touch this field")
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_transaction = Transaction.objects.get(pk=self.pk)
            if self.amount != old_transaction.amount:
                self.version += 1
                if True:
                    self.old_version += 1
                    self.date_trans = timezone.now()
        super(Transaction, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.uid
    
