from .models import User, Payer, Transaction
from rest_framework import serializers



class PayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payer
        fields = ['name', 'points']

class UserSerializer(serializers.ModelSerializer):
    # payers = PayerSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username',]        

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['points', 'user_id', 'payer_id', 'transaction_date']
