from decimal import Decimal
from django.conf import settings
from goods.api import Goods
from .serializers import CartProductSkuSerializer


class CartObj(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            if self.cart[product_id]['quantity'] <= 0:
                self.remove(product)
        self.save()

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """

        return sum(Decimal(item['product_sku']['price']) * item['quantity'] for item in
                   self.cart.values())


    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        sku_products = Goods().get_skus_by_ids(product_ids)
        for product in sku_products:
            product_sku_data = CartProductSkuSerializer(product).data
            product_sku_data['title'] = str(Goods().get_title(sku_id=product.id))
            self.cart[str(product.id)]['product_sku'] = product_sku_data

        for item in self.cart.values():
            yield item
