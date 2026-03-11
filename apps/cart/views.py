from django.shortcuts import render, redirect
from .cart import Cart
from apps.products.models import SanPhamChiTiet


def cart_detail(request):

    cart = request.session.get('cart', {})

    products = []

    for product_id, item in cart.items():

        product = SanPhamChiTiet.objects.get(pk=product_id)

        products.append({
            "product": product,
            "quantity": item['quantity']
        })

    return render(request, 'cart.html', {'products': products})


def add_to_cart(request, product_id):

    cart = Cart(request)

    cart.add(product_id)

    return redirect('cart')


def remove_from_cart(request, product_id):

    cart = Cart(request)

    cart.remove(product_id)

    return redirect('cart')


def update_cart(request, product_id):

    quantity = int(request.POST.get('quantity'))

    cart = Cart(request)

    cart.update(product_id, quantity)

    return redirect('cart')