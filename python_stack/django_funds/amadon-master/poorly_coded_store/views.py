from django.shortcuts import render, redirect
from .models import Order, Product


def index(request):
    if 'Cart' not in request.session:
        request.session['Cart'] = []

    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def checkout(request):
        if 'Cart' not in request.session:
            request.session['Cart'] = []

        if request.method == 'POST':
            product = Product.objects.get(id=request.POST['product_id'])
            _order = Order.objects.create(
                quantity_ordered=int(request.POST["quantity"]),
                total_price=int(request.POST["quantity"]) * product.price
            )
            _order.save()

            totalQuantity = 0
            totalPaid = 0
            all_orders = Order.objects.all()

            for order in all_orders:
                totalQuantity += order.quantity_ordered
                totalPaid += order.total_price

            context = {
                "lastOrderPrice":int(request.POST['quantity']) * float(product.price),
                "totalQuantity":totalQuantity,
                "totalPaid":totalPaid
            }

            del request.session['Cart']

            return render(request, "store/checkout.html",context)
        else:
            return redirect('/')