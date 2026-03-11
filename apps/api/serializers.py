from rest_framework import serializers
from apps.products.models import SanPham

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model=SanPham

        fields="__all__"