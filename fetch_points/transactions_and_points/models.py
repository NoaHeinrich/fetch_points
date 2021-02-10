from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Payer(models.Model):
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0) 
    users = models.ManyToManyField(User, through='Transaction', related_name='payers')

    @classmethod
    def order_by_oldest_transaction(cls):
        return cls.objects.order_by('transactions__transaction_date')

    def __str__(self):
        return f'{self.name}: {self.points} points'       
class Transaction(models.Model):
    points = models.IntegerField()
    transaction_date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    payer_id = models.ForeignKey(Payer, on_delete=models.CASCADE, related_name='transactions')

    def __str__(self):
        return f'Points: {self.points}, Date: {self.transaction_date}'


