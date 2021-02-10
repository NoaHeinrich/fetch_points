from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Transaction, Payer
import json
from .serializers import UserSerializer, PayerSerializer, TransactionSerializer
from .forms import UserForm
from datetime import date
# Create your views here.
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    serialized_user = UserSerializer(user)
    payers = user.payers.distinct().filter(points__gt=0)
    serialized_payers = PayerSerializer(payers, many=True)
    return JsonResponse(data={'user': serialized_user.data, 'payers': serialized_payers.data}, status=200, safe=False)

@csrf_exempt
def new_user(request):
    if request.method == 'POST':
        # data = json.load(dict(request.POST))
        # print(data)
        form = UserForm(dict(request.POST))
        if form.is_valid():
            user = form.save(commit=True)
            serialized_user = UserSerializer(user)
            return JsonResponse(data=serialized_user.data, status=200)

@csrf_exempt
def add_points(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        print(request.POST)
        payer, created = Payer.objects.get_or_create(name=request.POST['payer'])
        print(payer)
        transaction = Transaction(points=int(request.POST['points']), payer_id=payer, user_id=user, transaction_date=date.today())
        transaction.save()
        payer.points += int(request.POST['points'])
        payer.save()
        return JsonResponse(data=TransactionSerializer(transaction).data, status=200)

@csrf_exempt        
def deduct_points(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        ordered_payers = user.payers.order_by('transactions__transaction_date').distinct()
        payment = int(request.POST['points'])
        transactions = []
        for payer in ordered_payers:
            if payment > 0:
                transaction = ''
                if payment >= payer.points and payer.points > 0:
                    payment -= payer.points
                    transaction = Transaction(payer_id=payer, user_id=user, points= -payer.points, transaction_date=date.today())
                    # transaction.points = -payer.points
                    payer.points = 0
                else:
                    payer.points -= payment
                    transaction = Transaction(payer_id=payer, user_id=user, points= -payment, transaction_date=date.today())
                    # transaction.points = -payment
                    payment = 0
                transaction.save()
                transactions.append(transaction)
                payer.save()
        serialized_transactions = TransactionSerializer(transactions, many=True)
        return JsonResponse(data=serialized_transactions.data, status=200, safe=False)



