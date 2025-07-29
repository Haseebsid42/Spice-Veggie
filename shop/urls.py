from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('spices/', views.product_list, name='product_list'),
    path('vegetables/', views.vegetable_list, name='vegetable_list'),
    path('fruits/', views.fruit_list, name='fruit_list'),
    path('add-to-cart/<str:item_type>/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:fruit_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<str:item_type>/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<str:item_type>/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('signup/', views.sign_up, name='sign_up'),
    path('search/', views.search_view, name='search'),



    
]
