from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request,order_id):
    orders = Order.objects.all()
    total = 0
    for order in orders:
        total = order.total_price + total
    context = {
        "order": Order.objects.get(id=order_id),
        "total": total,
        "count": Order.objects.all()
    }
    return render(request, "store/checkout.html",context)


def new_order(request):
    product = Product.objects.get(id=(request.POST['price']))
    quantity = request.POST["quantity"]
    order_total = product.price * int(quantity)
    new_order = Order.objects.create(quantity_ordered=quantity, total_price=order_total)
    order_id = new_order.id
    return redirect("/checkout/{}".format(order_id))