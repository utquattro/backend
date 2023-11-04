from .models import Phone
from .serializers import LogoSerializer, PaySystemSerializer, PhoneSystemSerializer, \
    CopyrightSystemSerializer, SocicalSystemSerializer




def main_page_setup():

    response_data = {
        'logo': 'asd'
    }
    return response_data


# def create_test_value():
#     Socical.objects.bulk_create([Socical(name='telegram',
#                                          link='https://t.me/durov',
#                                          description='ссылка на телегу',
#                                          img_url='images/shop_settings/social/telegram.svg',
#                                          active=True),
#                                  Socical(name='vk',
#                                          link='vk.com/id1',
#                                          description='страничка магазина в вк',
#                                          img_url='images/shop_settings/social/vk.svg',
#                                          active=True)])
#
#     PaySystem.objects.bulk_create([PaySystem(pay_system_name='troy',
#                                              img_url='images/shop_settings/pay_system/troy.svg',
#                                              active=True),
#                                    PaySystem(pay_system_name='master_card',
#                                              img_url='images/shop_settings/pay_system/mastercard.svg',
#                                              active=True),
#                                    PaySystem(pay_system_name='visa',
#                                              img_url='images/shop_settings/pay_system/visa.svg',
#                                              active=True)])
#
#     Phone.objects.bulk_create([Phone(number='+7(800) 800-80-80',
#                                      description='справочная служба',
#                                      active=True,
#                                      position=1),
#                                Phone(number='+7(999) 999-99-99',
#                                      description='интернет-магазин',
#                                      active=True,
#                                      position=2)])
#     a = Copyright.objects.create(name='copyright',
#                                  description='© 2023 Любое использование контента без письменного '
#                                              'разрешения запрещено',
#                                  active=True)
#     a.save()
#     b = Logo.objects.create(title='logo',
#                             description='Логотип магазина',
#                             logo_url='images/shop_settings/logo/logo.png',
#                             active=True)
#     b.save()



