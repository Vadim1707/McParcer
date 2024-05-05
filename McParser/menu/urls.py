from rest_framework.routers import SimpleRouter
from .views import AllProductsViewSet


router = SimpleRouter()
router.register("all_products", AllProductsViewSet)

# a) get: /all_products/  - return all information about all products
# b) get: /products/{product_name}  - return information about exact product
# c) get: //products/{product_name}/{product_field}  - return information about exact field      exact product

urlpatterns = router.urls
