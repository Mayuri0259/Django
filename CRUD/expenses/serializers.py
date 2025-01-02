from rest_framework import serializers
from .models import Transactions

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            "id",
            "title",
            "amount",
            "transaction_type",
        ]

    # serialize all attributes 
       # fields = '__all__'

    # serialize all attributes excluding these
       # exclude = ['transaction_type', 'amount']

