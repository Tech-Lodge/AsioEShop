from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product
from rest_framework import status


# Create your views here.

#localhost:8080/store/products
#localhost:8080/store/products/1

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
