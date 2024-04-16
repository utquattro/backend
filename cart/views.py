from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer, CartAddItemSerializer, CartDeleteSerializer
from .api import CartObj


class UserCartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = ([TokenAuthentication])

    def get(self, request):
        cart = CartObj(request)
        cart_items = cart.get_cart_info(request=request)
        return Response(cart_items)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = ([TokenAuthentication])

    def post(self, request):
        try:
            new_cart = CartObj(request)
            serializer = CartAddItemSerializer(data=request.data)
            if serializer.is_valid():
                valid_data = serializer.data
                product_id = valid_data['product']
                quantity = valid_data['quantity']
                ff = new_cart.add(product_id=product_id, quantity=quantity, update_quantity=True)
                return Response(new_cart.get_cart_info(request=request), status=200)

            return Response(serializer.errors, status=400)
        except KeyError as e:
            return Response({'error': str(e)}, status=400)


class DeleteToCartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = ([TokenAuthentication])

    def post(self, request):
        try:
            new_cart = CartObj(request)
            serializer = CartDeleteSerializer(data=request.data)
            if serializer.is_valid():
                valid_data = serializer.data
                product_id = valid_data['product_id']
                ff = new_cart.remove(product=product_id)
                return Response(new_cart.get_cart_info(request=request), status=200)

            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist as e:
            return Response({'error': f"{product_id}  не найден в корзине"}, status=400)


class ClearCartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = ([TokenAuthentication])

    def post(self, request):
        try:
            new_cart = CartObj(request)
            ff = new_cart.clear()
            return Response(new_cart.get_cart_info(request=request), status=200)

        except ObjectDoesNotExist as e:
            return Response({'error': f"{e}"}, status=400)
