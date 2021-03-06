from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """A view to show the shopping cart"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Add quantity of the product to shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """
    Adjust the quantity of product in the cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id)

    request.session['cart'] = cart
    print(quantity)
    return redirect(reverse('view_cart'))
