from django.http import HttpResponse
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient

# Create your views here.
def index(request):
    cl = MpesaClient()
    phone_number = ''
    amount = 10
    account_reference = 'reference'
    transaction_desc = 'description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number,amount,account_reference,transaction_desc)
    return HttpResponse(response)
def stk_push_callback(request):
    data = request.body
    return HttpResponse('Stk push in Django')
