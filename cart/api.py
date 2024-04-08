from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import get_object_or_404

from cart.models import Cart, CartItem
from goods.api import Goods


class CartObj(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.user_id = request.user
        cart = Cart.objects.filter(user=self.user_id).first()
        if not cart:
            # save an empty cart in the session
            cart = Cart.objects.create(user=self.user_id)
        self.cart_id = cart
        self.cart_items = CartItem.objects.filter(cart=self.cart_id).order_by('created_at')

    def add(self, product_id, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        add_product = Goods().get_product_by_id(product_id)
        if add_product.stock <= quantity:
            return {'error': 1001, 'message': f"Переданное количество больше чем есть на складе"}
        try:
            tom = CartItem.objects.get(cart=self.cart_id, product=add_product.id)
            tom.quantity = quantity
            tom.save()
        except ObjectDoesNotExist:
            cart_item, created = CartItem.objects.get_or_create(cart=self.cart_id,
                                                                product=add_product,
                                                                quantity=quantity)
        except MultipleObjectsReturned:
            print("Найдено более одного объекта")

        return {'success': True, 'message': f"Продукт {add_product.name} добавлен в корзину."}

    def remove(self, product):
        """
        Удаление товара из корзины.
        """

        f = CartItem.objects.get(cart=self.cart_id, product=product)
        f.delete()
        return {'success': True, 'message': f"Продукт {product} удален."}



    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        print('len start')
        return sum(item['quantity'] for item in self.cart_items.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        sum = 0
        for i in self.cart_items.values():
            good = Goods().get_product_by_id(i['product_id'])
            quan = i['quantity']
            sum = sum + (good.price * quan)

        return sum



