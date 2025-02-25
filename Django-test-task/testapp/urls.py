from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:id>/', views.item_detail, name='item-detail'),
    path('buy/<int:id>/', views.buy_item, name='buy-item'),
    path('order/<int:id>',views.order_detail, name='order-detail'),
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart_detail, name='cart-detail'),
    path('buy/order/<int:order_id>/', views.buy_order, name='buy-order'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update-cart-item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('success/', views.main_page, name='main-page'),
    path("", views.main_page, name='main-page'),
]