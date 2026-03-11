from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('apps.products.urls')),   # trang chủ

    path('admin/', admin.site.urls),

    path('products/', include('apps.products.urls')),
    path('cart/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
]