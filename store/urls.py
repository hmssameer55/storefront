from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')


products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
# lookup is the name of the field in the Product model that we want to use to lookup the product
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
products_router.register('images', views.ProductImageViewSet,
                         basename='product-images')
# we write basename because we have overridden default queryset in ProductImageViewSet

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + products_router.urls + carts_router.urls
