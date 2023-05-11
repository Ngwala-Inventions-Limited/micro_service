from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('uid','amount', 'register')
    readonly_fields=('version', 'old_version', 'date_trans')


admin.site.register(Transaction, TransactionAdmin)    

