from django.urls import path, include
from products.routes import ROUTES
from products.views.category_views import get_category
from products.views.brand_views import get_brand
from products.views.product_views import get_products, get_products_details
# from main.ecomBackend.products.models import ProduProducts

urlpatterns = [
    path(ROUTES["get_category"], get_category),
    path(ROUTES["get_brands"], get_brand),
    path(ROUTES["get_products"], get_products),
    path( f"{ROUTES['product_details']}<uuid:id>/",  get_products_details, name="product-category-list-view"),

    # path(ROUTES["product_category_list"], product_list_category),
    # path(f"{ROUTES['udpate_product_category']}<uuid:id>/", update_product_category),
    # path(f"{ROUTES['delete_product_category']}<uuid:id>/", delete_product_category),

    # path(ROUTES["add_product_brand"], create_product_brand, name="product-category-create-view"),
    # path(ROUTES["product_brand_list"], product_brand_list,name="product-category-list-view"),
    # path(f"{ROUTES['udpate_product_brand']}<uuid:id>/", update_product_brand, name="product-category-list-view"),
    # path( f"{ROUTES['delete_product_brand']}<uuid:id>/",  delete_product_brand, name="product-category-list-view"),

    # path(ROUTES["product_list"], create_product, name="product-category-create-view"),
    # path(ROUTES["product_create"], product_list, name="product-category-list-view"),
    # path( f"{ROUTES['product_view']}<uuid:id>/",  delete_product, name="product-category-list-view"),
    # path(f"{ROUTES['product_update']}<uuid:id>/", update_product, name="product-category-list-view"),

]
