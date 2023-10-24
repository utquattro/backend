from rest_framework import routers
from goods.views import TestListAPIView


router = routers.DefaultRouter()
router.register('', TestListAPIView, 'category')


urlpatterns = router.urls


