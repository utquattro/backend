from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from goods.models import ProductSku
from .api import CartObj
from .models import Cart, CartItem
from goods.api import Goods
from .serializers import CartSerializer, CartItemSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.sessions.models import Session
from django.views.decorators.http import require_POST


@api_view(['POST'])
def cart_add(request):
    try:
        new_cart = CartObj(request)
        product = get_object_or_404(ProductSku, id=request.data['product_sku_id'])
        if product:
            new_cart.add(product=product, quantity=request.data['quantity'], update_quantity=True)
            return Response({'cart': new_cart.cart})
        return Response({'error'})
    except KeyError as e:
        return Response({'error': str(e)}, status=400)


@api_view(['GET'])
def cart_detail(request):
    try:
        new_cart = CartObj(request)

        return Response({'cart': new_cart.cart})
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['DELETE'])
def cart_remove(request):
    try:
        new_cart = CartObj(request)
        new_cart.remove(request.data['product_sku_id'])
        product = get_object_or_404(ProductSku, id=request.data['product_sku_id'])
        if product:
            new_cart.add(product=product, quantity=request.data['quantity'], update_quantity=True)
            return Response({'cart': new_cart.cart})
        return Response({'error'})
    except KeyError as e:
        return Response({'error': str(e)}, status=400)


# @api_view(['POST'])
# def create_cart(request):
#     cart1 = CartObj(request)
#     session = cart1.session.session_key
#     print('asdasdas', session)
#     cart = Cart.objects.filter(session=session).first()
#
#     if not cart:
#         cart = Cart.objects.create(session=session)
#
#     data = request.data.get('items')
#
#     if data:
#         for item in data:
#             product_sku = get_object_or_404(ProductSku, id=item.get('product_sku'))
#             quantity = item.get('quantity')
#             CartItem.objects.create(product_sku=product_sku, quantity=quantity, cart=cart)
#
#     return Response({'message': 'Cart created successfully'})

# @api_view(['POST', 'GET'])
# def cart(request):
#     if request.method == 'POST':
#         d = request.session
#         product_sku = request.data
#         #serializer = CartItemSerializer(data=product_sku)
#         #if serializer.is_valid():
#         return Response({"asd": d})
#         #return Response(serializer.errors, status=400)
#
#     elif request.method == 'GET':
#         # Access query parameters
#         #query_params = request.query_params
#         #cart1 = CartObj(request)
#
#         print(123)
#         # Perform some logic with the query params and cookies
#
#         return Response({1})
#
#
#
# class CartCreateView(APIView):
#     def post(self, request):
#         cart1 = CartObj(request)
#         serializer = CartSerializer(data=request.data)
#         if serializer.is_valid():
#             cart = serializer.save()
#             return Response({'cart_id': cart.id}, status=201)
#         return Response(serializer.errors, status=400)