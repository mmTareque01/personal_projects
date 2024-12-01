from django.urls import path, include
from products.routes import ROUTES
from products.views.category_views import create_product_category, product_list_category, update_product_category, delete_product_category
from products.views.brand_views import create_product_brand, product_brand_list, update_product_brand, delete_product_brand
from products.views.product_views import create_product, product_list, view_product, update_product, delete_product
# from main.ecomBackend.products.models import ProduProducts

urlpatterns = [
    # path("products/", include('products.urls')),
    path(ROUTES["add_product_category"], create_product_category),
    path(ROUTES["product_category_list"], product_list_category),
    path(f"{ROUTES['udpate_product_category']}<uuid:id>/", update_product_category),
    path(f"{ROUTES['delete_product_category']}<uuid:id>/", delete_product_category),

    path(ROUTES["add_product_brand"], create_product_brand, name="product-category-create-view"),
    path(ROUTES["product_brand_list"], product_brand_list,name="product-category-list-view"),
    path(f"{ROUTES['udpate_product_brand']}<uuid:id>/", update_product_brand, name="product-category-list-view"),
    path( f"{ROUTES['delete_product_brand']}<uuid:id>/",  delete_product_brand, name="product-category-list-view"),

    path(ROUTES["product_list"], product_list, name="product-category-create-view"),
    path(ROUTES["product_create"], create_product, name="product-category-list-view"),
    path( f"{ROUTES['product_view']}<uuid:id>/",  delete_product, name="product-category-list-view"),
    path(f"{ROUTES['product_update']}<uuid:id>/", update_product, name="product-category-list-view"),
    path( f"{ROUTES['product_delete']}<uuid:id>/",  delete_product, name="product-category-list-view"),

]
