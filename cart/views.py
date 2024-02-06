from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .api import CartObj
from goods.api import Goods
from .serializers import CartAddItemSerializer, CartSerializer, CartItemSkuSerializer, CartItemSerializer


@authentication_classes([SessionAuthentication])
@api_view(['GET'])
def cart_view(request):
    try:
        cart = CartObj(request).cart
        print(cart)
        items = {"cart": cart,
                 "count": 'общее количество',
                 "total_price": 'общий прайс'}
        return Response(items, status=200)
    except KeyError as e:
        return Response({'error': str(e)}, status=400)



@api_view(['POST'])
def cart_add(request):
    try:
        new_cart = CartObj(request)
        serializer = CartAddItemSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data
            product_id = valid_data['product_id']
            quantity = valid_data['quantity']
            product = Goods().get_sku_by_id(sku_id=product_id)
            if product:
                if quantity <= product.stock:
                    new_cart.add(product=product, quantity=quantity, update_quantity=True)
                    return Response({'status': f'ok'}, status=200)
                return Response({'error': 1001, 'message': f"Переданное количество больше чем есть на складе"},
                                status=400)
            return Response({'error': f'product:{product} not found'})
        return Response(serializer.errors, status=400)
    except KeyError as e:
        return Response({'error': str(e)}, status=400)


@api_view(['POST'])
def cart_remove(request):
    try:
        new_cart = CartObj(request)
        product = Goods().get_sku_by_id(sku_id=request.data['product_id'])
        if product:
            new_cart.remove(product)
            # ff = CartDetailAPIView().retrieve(request).data
            return Response({"ok"}, status=200)
        return Response({'error'})
    except KeyError as e:
        return Response({'error': str(e)}, status=400)

#
# class CartDetailAPIView(RetrieveAPIView):
#     serializer_class = CartSerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         try:
#             new_cart = CartObj(request)
#             cart_list = []
#             return Response(new_cart.cart, status=200)
#         except Exception as e:
#             return Response({str(e)}, status=400)
