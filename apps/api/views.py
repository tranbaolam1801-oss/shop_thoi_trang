from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.products.models import SanPham
from .serializers import ProductSerializer


@api_view(["GET"])

def products_api(request):

    products=SanPham.objects.all()

    serializer=ProductSerializer(products,many=True)

    return Response(serializer.data)