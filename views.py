from django.shortcuts import render, redirect

from .models import Payment, Order 
from sw_utils.sw_currency.models import Currency

from django.http import JsonResponse 


def liqpay_callback(request):
  from liqpay.utils import create_liqpay_transaction
  # if request.method == 'GET':
  #   return JsonResponse({'Hello':'Hello'})
  print('liqpay_callback!!!!!!!')
  form          = create_liqpay_transaction(request)
  transaction   = form.instance
  print(transaction)
  print(transaction.order_id)
  order = Order.objects.get(id=transaction.order_id)
  payment       = Payment.objects.create(
    order=order,
    amount=transaction.amount,
    currency=Currency.objects.get(code=transaction.currency)
  )
  order.make_order(request)
  return redirect('thank_you')




