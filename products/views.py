from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser

# Create your views here.
class ProductListAPIView(APIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            # POST 요청인 경우에는 인증
            return [IsAuthenticated()]
        return []
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ProductDetailAPIView(APIView):

    def get_permissions(self): #로그인 인증 
        if self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsAuthenticated()]
        return []

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if request.user == product.author:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, pk):
        if request.user == product.author:
            product = get_object_or_404(Product, pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)