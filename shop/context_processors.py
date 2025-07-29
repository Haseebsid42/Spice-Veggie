from decimal import Decimal

def cart_count(request):
    cart = request.session.get('cart', {})
    total_quantity = sum(int(qty) for qty in cart.values())
    return {'cart_count': total_quantity}
