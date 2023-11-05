from django.urls import path
from goods.views import GetAllCategory, GetAllBrands, GetCategoryProducts,GetProductWithCategory

urlpatterns = [

    path('brand/', GetAllBrands.as_view()),
    path('category/', GetAllCategory.as_view()),
    path('category/<slug:category_slug>/', GetCategoryProducts.as_view()),
    path('category/<slug:category_slug>/<slug:product_slug>/', GetProductWithCategory.as_view()),

]

