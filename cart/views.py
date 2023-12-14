from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .api import CartObj
from goods.api import Goods
from .serializers import CartAddItemSerializer, CartSerializer, CartItemSkuSerializer, CartItemSerializer


class CartDetailAPIView(RetrieveAPIView):
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            new_cart = CartObj(request)
            cart_list = []
            if len(new_cart) > 0:
                for i in new_cart:
                    cart_list.append(i)
                if cart_list:
                    resp = {
                        'items': cart_list,
                        'items_count': len(new_cart),
                        'total_price': new_cart.get_total_price()
                    }
                    return Response(resp, status=200)
            return Response({'code': "900",
                             'message': "cart is empty"}, status=200)
        except Exception as e:
            return Response({'error': 777, 'message': str(e)}, status=400)


@api_view(['POST'])
def cart_add(request):
    try:
        new_cart = CartObj(request)
        serializer = CartAddItemSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data
            sku_id = valid_data['product_sku_id']
            quantity = valid_data['quantity']
            print('yes')
            product = Goods().get_sku_by_id(sku_id=sku_id)
            if product:
                if quantity <= product.stock:
                    new_cart.add(product=product, quantity=quantity, update_quantity=True)
                    ff = CartDetailAPIView().retrieve(request).data
                    return Response(ff, status=200)
                return Response({'error': 1001, 'message': f"Переданное количество больше чем есть на складе"},
                                status=400)
            return Response({'error': f'product:{product} not found'})
        print('ops', serializer.data)
        return Response(serializer.errors, status=400)
    except KeyError as e:
        return Response({'error': str(e)}, status=400)


@api_view(['POST'])
def cart_remove(request):
    try:
        new_cart = CartObj(request)
        product = Goods().get_sku_by_id(sku_id=request.data['product_sku_id'])
        if product:
            new_cart.remove(product)
            ff = CartDetailAPIView().retrieve(request).data
            return Response(ff, status=200)
        return Response({'error'})
    except KeyError as e:
        return Response({'error': str(e)}, status=400)
