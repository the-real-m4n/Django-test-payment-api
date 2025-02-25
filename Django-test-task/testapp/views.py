import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, Http404
from .models import Item ,Order , OrderItem
import stripe
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, id):
    """
    Initiates a Stripe checkout session for purchasing an item.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The primary key of the item to be purchased.

    Returns:
        JsonResponse: A JSON response containing the Stripe session ID.

    Raises:
        Http404: If the item with the given id does not exist.
    """
    item = get_object_or_404(Item, pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),#  конвертируем цену из копеек в рубли
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return JsonResponse({'session_id': session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item_detail.html', {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })

def order_detail(request, id):
    order = get_object_or_404(Order, pk=id)
    return render(request, 'order_detail.html', {
        'order': order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })

def buy_order(request, order_id):
    try:
        order = get_object_or_404(Order, pk=order_id)
    except Http404:
        logging.error(f"Order with id {order_id} not found.")
        return JsonResponse({'error': 'Order not found'}, status=404)
    
    # Создаем Stripe сессию для всей корзины


    line_items = []
    for order_item in order.orderitem_set.all():
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': order_item.item.name},
                'unit_amount': int(order_item.item.price * 100),
            },
            'quantity': order_item.quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    
    # Помечаем заказ как оплаченный
    order.is_active = False
    order.delete()
    
    # Очищаем корзину
    if 'cart_id' in request.session:
        del request.session['cart_id']
    
    return JsonResponse({'session_id': session.id})



# views.py
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    order_id = request.session.get('cart_id')
    if order_id:
        order = get_object_or_404(Order, pk=order_id, is_active=True)
    else:
        order = Order.objects.create()
        request.session['cart_id'] = order.id
    
    # Проверяем, есть ли товар уже в корзине
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        item=item,
        defaults={'quantity': 1}
    )
    
    if not created:
        order_item.quantity += 1
        order_item.save()
    
    messages.success(request, f'Товар "{item.name}" добавлен в корзину')
    return redirect('item-detail', id=item_id)

def cart_detail(request):
    order_id = request.session.get('cart_id')
    
    if order_id:
        order = get_object_or_404(Order, pk=order_id, is_active=True)
    else:
        order = None
    
    return render(request, 'cart_detail.html', {'order': order,
                                                'stripe_public_key': settings.STRIPE_PUBLIC_KEY })

@require_POST
def update_cart_item(request, item_id):
    order = get_object_or_404(Order, pk=request.session.get('cart_id'))
    order_item = get_object_or_404(OrderItem, order=order, item_id=item_id)
    
    data = json.loads(request.body)
    order_item.quantity = data['quantity']
    order_item.save()
    
    return JsonResponse({'status': 'success'})

@require_POST
def remove_from_cart(request, item_id):
    order = get_object_or_404(Order, pk=request.session.get('cart_id'))
    OrderItem.objects.filter(order=order, item_id=item_id).delete()
    
    return JsonResponse({'status': 'success'})