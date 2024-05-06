from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import AllProductsViewSet, ProductViewSet, ProductDetailViewSet


router = SimpleRouter()
router.register("all_products", AllProductsViewSet)

# a) get: /all_products/  - return all information about all products
# b) get: /products/{product_name}  - return information about exact product
# c) get: //products/{product_name}/{product_field}  - return information about exact field      exact product

urlpatterns = router.urls

urlpatterns += [
    path("products/<str:product_name>/", ProductViewSet.as_view()),
    path("products/<str:product_name>/<str:product_field>/", ProductDetailViewSet.as_view()),
]