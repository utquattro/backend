from .models import  Socical, PaySystem,  MarketingBanner, Settings
from django.shortcuts import get_list_or_404, get_object_or_404


class ShopSetting:
    def __init__(self):
        self.active_settings = Settings.active_objects
        self.active_marketing_banner = MarketingBanner.active_objects


