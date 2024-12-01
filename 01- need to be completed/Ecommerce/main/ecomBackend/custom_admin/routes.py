from products.routes import ROUTES as p_routes
from users.routes import ROUTES as u_routes

MAIN_ROUTES = {
    "admin": "admin",
    "dashboard": "dashboard",
    "email": "email",
    "chat": "chat",
    "todo": "todo",
    "kanban": "kanban",
    "calendar": "calendar",
    "file_manager": "file-manager",

    "invoice_create": "invoice/create",
    "invoice_edit": "invoice/edit",
    "invoice_list": "invoice/list",
    "invoice_preview": "invoice/preview",
    "invoice_print": "invoice/print",



    "product_list": "product/list",
    "product_create": "product/create",
    "product_update": "product/update",
    "product_delete": "product/delete",
    "product_view": "product/view",
    # "add_product_category": "/admin/prodcut/list",

}

ROUTES = {
    "admin": MAIN_ROUTES["admin"],
    "dashboard": f"/{MAIN_ROUTES['admin']}/{MAIN_ROUTES['dashboard']}",
    "email": f"/{MAIN_ROUTES['admin']}/{MAIN_ROUTES['email']}",
    "chat": f"/{MAIN_ROUTES['admin']}/{MAIN_ROUTES['chat']}",
    "todo": f"/{MAIN_ROUTES['admin']}/todo",
    "kanban": f"/{MAIN_ROUTES['admin']}/kanban",
    "calendar": f"/{MAIN_ROUTES['admin']}/calendar",
    "file_manager": f"/{MAIN_ROUTES['admin']}/file-manager",
    "invoice_create": f"/{MAIN_ROUTES['admin']}/invoice/create",
    "invoice_edit": f"/{MAIN_ROUTES['admin']}/invoice/edit",
    "invoice_list": f"/{MAIN_ROUTES['admin']}/invoice/list",
    "invoice_preview": f"/{MAIN_ROUTES['admin']}/invoice/preview",
    "invoice_print": f"/{MAIN_ROUTES['admin']}/invoice/print",

    "product_category_list": f"/{MAIN_ROUTES['admin']}/{p_routes['product_category_list']}",
    "add_product_category": f"/{MAIN_ROUTES['admin']}/{p_routes['add_product_category']}",
    "update_product_category": f"/{MAIN_ROUTES['admin']}/{p_routes['udpate_product_category']}",
    "delete_product_category": f"/{MAIN_ROUTES['admin']}/{p_routes['delete_product_category']}",

    "product_brand_list": f"/{MAIN_ROUTES['admin']}/{p_routes['product_brand_list']}",
    "add_product_brand": f"/{MAIN_ROUTES['admin']}/{p_routes['add_product_brand']}",
    "update_product_brand": f"/{MAIN_ROUTES['admin']}/{p_routes['udpate_product_brand']}",
    "delete_product_brand": f"/{MAIN_ROUTES['admin']}/{p_routes['delete_product_brand']}",

    "product_list": f"/{MAIN_ROUTES['admin']}/{MAIN_ROUTES['product_list']}",
    "product_create": f"/{MAIN_ROUTES['admin']}/{MAIN_ROUTES['product_create']}",
    "product_update": f"/{MAIN_ROUTES['admin']}/{MAIN_ROUTES['product_update']}",
    "product_delete": f"/{MAIN_ROUTES['admin']}/{MAIN_ROUTES['product_delete']}",
    "product_view": f"/{MAIN_ROUTES['admin']}/{MAIN_ROUTES['product_view']}",


    "user_list": f"/{MAIN_ROUTES['admin']}/{u_routes['user_list']}",
    # "user_info": f"/{MAIN_ROUTES['admin']}/{u_routes['user_info']}",
    # "add_product_category": "/admin/prodcut/list",

}
