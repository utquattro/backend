from rest_framework import routers
from .views import MainPageSetup


router = routers.DefaultRouter()
router.register('', MainPageSetup, 'eshop_setup')


urlpatterns = router.urls


