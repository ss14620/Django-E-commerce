from django.shortcuts import render

# Create your views here.
import stripe

stripe.api_key = "sk_test_H5Twhb1IsrsJ8HiL7r0lrP7B"

STRIPE_PUB_KEY = "pk_test_HrnqD3p1uWo8WsZs83D1LJz8"
def payment_method_view(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'billing/payment-method.html',{"publish_key":STRIPE_PUB_KEY})
