from django.contrib import admin
from .models import User, Payer, Transaction
# Register your models here.
admin.site.register(User)
admin.site.register(Payer)
admin.site.register(Transaction)