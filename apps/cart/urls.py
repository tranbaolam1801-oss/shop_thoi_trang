from django.urls import path
from . import views

urlpatterns = [

    path('', views.cart_detail, name='cart'),

    path('add/<str:product_id>/', views.add_to_cart, name='add_cart'),

    path('remove/<str:product_id>/', views.remove_from_cart, name='remove_cart'),

    path('update/<str:product_id>/', views.update_cart, name='update_cart'),
]