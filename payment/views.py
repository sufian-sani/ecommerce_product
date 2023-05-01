from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# Create your views here.

# models

from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from order.models import Order, Cart

# view
from django.views.generic import TemplateView


class CheckoutTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)

        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order_item = order_qs[0].orderitems.all()
        order_total = order_qs[0].get_totals()

        context = {
            'billing_address':form,
            'order_item':order_item,
            'order_total':order_total,
        }
        return render(request, 'store/checkout.html', context)

    def post(self, request, *args, **kwargs):
        pass
