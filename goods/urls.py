from django.urls import path
from goods.views import GetAllCategory, GetAllBrands, GetCategoryProducts,GetProductSlugWithCategory, \
    GetProductWithId, GetAllSlider, ProductSkuView, RecommendedProduct, get_rec

urlpatterns = [

    path('brand/', GetAllBrands.as_view()),
    path('slider/', GetAllSlider.as_view()),
    path('category/', GetAllCategory.as_view()),
    path('category/<slug:category_slug>/', GetCategoryProducts.as_view()),
    path('category/<slug:category_slug>/<slug:product_slug>/', GetProductSlugWithCategory.as_view()),
    path('product/<slug:slug>/', GetProductWithId.as_view()),
    # path('product/', ProductSkuView.as_view()),
    path('products/recommended', get_rec),
    #path('products/rec', get_rec),
]

