
from django.contrib import admin
from django.urls import path, include
from .views.authentication import dashboard, login_view
from custom_admin.views.apps import email, chat, calendar, file_manger, kanban, todo
from custom_admin.views.invoice import create_invoice, invoice_edit, invoice_list, invoice_preview, invoice_print
from custom_admin.routes import MAIN_ROUTES

urlpatterns = [
    path("login", login_view, name="login-view"),
    path("dashboard", dashboard, name="dashboard-view"),

    # apps
    path("email", email, name="email-view"),
    path("chat", chat, name="chat-view"),
    path("todo", todo, name="todo-view"),
    path("calendar", calendar, name="calendar-view"),
    path("kanban", kanban, name="kanban-view"),
    path("file-manager", file_manger, name="file-manager-view"),

    #    Invoice
    path("invoice/create", create_invoice, name="invoice-create-view"),
    path("invoice/edit", invoice_edit, name="invoice-edit-view"),
    path("invoice/list", invoice_list, name="invoice-list-view"),
    path("invoice/preview", invoice_preview, name="invoice-preview-view"),
    path("invoice/print", invoice_print, name="invoice-print-view"),
    # path("email", email, name="email-view"),

    path("", include("products.urls.admin_urls")), #product uri
    path("", include("users.urls.admin_urls")), #users uri

]
