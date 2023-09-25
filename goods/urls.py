from rest_framework import routers
from goods.views import MainPageSetup


router = routers.DefaultRouter()
router.register('', MainPageSetup, 'category')


urlpatterns = router.urls


